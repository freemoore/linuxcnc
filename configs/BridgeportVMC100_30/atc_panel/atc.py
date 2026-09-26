# GladeVCP handler for the ATC tab: shows the magazine contents from the tool table.
# Random toolchanger: pocket 0 = spindle (shown on its own line). Pockets 1-30
# are in one column. The carousel's current pocket is bold.
import os
import linuxcnc
from gi.repository import GLib, Gdk, Gtk, Pango

class HandlerClass:
    def __init__(self, halcomp, builder, useropts):
        self.builder = builder
        self.store = builder.get_object("mag-store")
        self.car_pos = builder.get_object("car-pos")
        self.spindle = builder.get_object("mag-spindle")
        # Tighter rows so all pockets fit in one column
        # Compact style for the whole tab (this gladevcp process only), so the
        # tab fits with Axis at half screen width.
        css = Gtk.CssProvider()
        css.load_from_data(b"""
            * { font-size: 8pt; }
            button { padding: 1px 4px; min-height: 0; }
            spinbutton, spinbutton entry { min-height: 0; padding-top: 0; padding-bottom: 0; }
            frame > border { margin: 0; }
            #mag-view { -GtkTreeView-vertical-separator: 0; }
        """)
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), css,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        builder.get_object("mag-view").set_name("mag-view")
        ini = linuxcnc.ini(os.environ["INI_FILE_NAME"])
        self.tbl = os.path.join(os.path.dirname(os.environ["INI_FILE_NAME"]),
                                ini.find("EMCIO", "TOOL_TABLE") or "tool.tbl")
        self.pockets = int(ini.find("ATC", "POCKETS") or 30)
        self.last = None
        self.refresh()
        GLib.timeout_add(1000, self.refresh)

    def read_table(self):
        tools = {}
        with open(self.tbl) as f:
            for line in f:
                data, _, comment = line.partition(";")
                words = {w[0].upper(): w[1:] for w in data.split() if len(w) > 1}
                if "T" in words and "P" in words:
                    tools[int(words["P"])] = (int(words["T"]), comment.strip())
        return tools

    def refresh(self):
        try:
            pos = int(self.car_pos.hal_pin.get()) if self.car_pos is not None else 0
            key = (os.path.getmtime(self.tbl), pos)
            if key == self.last:
                return True
            self.last = key
            tools = self.read_table()
        except Exception as e:
            print("atc.py: cannot read tool table:", e)
            return True
        self.store.clear()
        bold, norm = Pango.Weight.BOLD, Pango.Weight.NORMAL
        for p in range(1, self.pockets + 1):
            t, desc = tools.get(p, (None, ""))
            self.store.append([str(p), "" if t is None else "T%d" % t, desc, bold if p == pos else norm])
        t, desc = tools.get(0, (None, ""))
        self.spindle.set_text("Spindle: " + ("empty" if t is None else "T%d  %s" % (t, desc)))
        return True

def get_handlers(halcomp, builder, useropts):
    return [HandlerClass(halcomp, builder, useropts)]
