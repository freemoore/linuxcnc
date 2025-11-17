if {[info proc tkgof] == ""} {
    rename tk_getOpenFile tkgof
}

proc tk_getOpenFile {args} {
    # Path to store the last-used directory
    set last_dir_file "$::env(HOME)/.last_file_dialog_dir"

    # Default to desktop
    set start_dir "$::env(HOME)/Desktop"

    # Try loading last-used directory
    if {[file exists $last_dir_file]} {
        set fh [open $last_dir_file r]
        set saved_dir [gets $fh]
        close $fh

        if {[file isdirectory $saved_dir]} {
            set start_dir $saved_dir
        }
    }

    set cmd "zenity --file-selection --filename=\"$start_dir/\""

    # Support -title if passed
    set idx [lsearch $args -title]
    if {$idx >= 0 && [llength $args] > $idx + 1} {
        set title [lindex $args [expr {$idx + 1}]]
        append cmd " --title=\"[string map {' ''} $title]\""
    }

    # Run Zenity and safely capture result
    set result ""
    if {[catch {exec sh -c $cmd} result] == 0} {
        # If a file was selected, save its directory
        if {[file exists $result]} {
            set dir [file dirname $result]
            set fh [open $last_dir_file w]
            puts $fh $dir
            close $fh
        }
    } else {
        # Zenity was cancelled or errored, set result to empty
        set result ""
    }

    return $result
}
