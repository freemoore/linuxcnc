# Bridgeport VMC1000-30: LinuxCNC retrofit

This is Andy's LinuxCNC config for a Bridgeport VMC1000-30 (4,400 kg). The original control was a Heidenhain TNC407. The machine has a 30-tool ATC and a Nikken CNC-201 4th axis (A).

The repo root is `~/linuxcnc`, which is shared with other machine configs. **Only work in this folder unless asked.**

`recent-work-summary-2026-09-24.md` holds the background and history: TNC MP values, 611 terminal wiring and the spindle parameter sheet. Where it disagrees with this file, this file wins. Where either disagrees with the live INI/HAL, **the live config wins**.

## Ground rules
- **ABSOLUTE: never change, create or delete any file without Andy's explicit OK first.** Show the proposed change (a diff for edits) before saving. This applies even to small fixes and to files Claude wrote itself.
- **ABSOLUTE: always make a backup before changing any file.** Copy it into this folder's `backups/`, named `<file>.<YYYY-MM-DD_HHMM>.bak`, and never overwrite an existing backup.
- **Don't commit without Andy's OK either.**
- **Never use PNCconf, and never suggest it.** This config is customised well beyond what PNCconf can handle, and running it would overwrite hand edits.
- **Never start LinuxCNC, `halrun` or `halcmd` against the real hardware, or do anything that could enable drives or move the machine, unless Andy asks.** Reading files and static checks are fine.
- **Don't rename HAL signals.** Use full descriptive names (e.g. `output-tool-magazine-fwd`). An older scheme of short abbreviations (`tlmagdir`, `mag_counter`, …) was retired and must not come back.
- **When the config disagrees with notes, report it. Don't "fix" it.**
- This is a new conversion being brought up. The older Bridgeport Series 2 Interact 2 (`../Bridgeport_AJM`) is the working production machine next door, so don't touch its config. Once this machine is reliable, AJM will be rebuilt too, and the two will run side by side: AJM for aluminium, VMC for steel.

## Hardware
- **Control:**
  - Mesa 7i97T (CARD0), with a 7i84U (CARD1) for I/O and a 7i74.
  - The config was adapted from the Morbidelli setup in `../morb01`.
  - Servo period is 1 ms.
- **Axis drives:** Siemens Simodrive 611 with analogue interface (6SN1118-0AA11-0AA1 control cards).
  - Pulse enable (663) is strapped to +24 V (terminal 9), so it's always asserted.
  - The 7i97T analogue enable is tied to the machine's original X/Y/Z enable signals.
- **Axis motors:** Siemens 1FT5066-0AC71, 2000 rpm rated. The tacho and rotor position sensor are wired to the drive, not to LinuxCNC.
- **Encoders:** AEDL differential quadrature, 5000 lines, giving 20000 counts/rev. The hostmot2 encoder filter is **off** on all encoders (on PCW's advice).
- **A drive:** Control Techniques Midi Maestro, separate from the 611 system.
- **Spindle:**
  - Drive: 611 80A power module with analogue control on pwmgen 05, and encoder feedback on encoder 05.
  - Single range, 40–6000 rpm. M19 orient works.

## Axes
| Joint | Axis | Notes |
|---|---|---|
| 0 | X | Tuned. 16 mm lead, ENCODER_SCALE −1250 (confirmed). Homes normally and latches on the encoder index. HOME_SEQUENCE 2 |
| 1 | Y | **Out of service.** See below |
| 2 | Z | Tuned. 10 mm lead, ENCODER_SCALE −2000. Homes normally and latches on the encoder index. HOME_SEQUENCE 1 |
| 3 | A | ENCODER_SCALE −5000 counts/degree (90:1 worm). **No home switch, by design.** Rotation is unlimited, and the high-ratio worm can't be moved by hand, so the position carries over between sessions via `position.txt`. When a true zero is needed, it's set by lining up the vernier marks by eye |

**Y status:** the motor is uncoupled and on the bench, waiting for either a repaired rotor-position hall sensor (Siemens 2AV63 7315) or a replacement motor. Andy decides which.
- Y is **disabled in hardware**: its enable and analogue-out cables are disconnected, so the drive can't be enabled or receive a setpoint.
- Joint 1 stays in the INI/HAL with derated values on purpose. Don't treat that as a bug.

## ATC
- **Mechanism:** SIDEPAL HL-20 double-arm changer:
  - round 30-pocket carousel
  - twin-gripper swing arm with a pneumatic drop
  - geneva cam driven by a motor with a brake override
- **Magazine control:**
  - The magazine is driven by the LinuxCNC `carousel` component in index mode.
  - `sense-0` is `input-tool-magazine-index-pulse` (7i84 input 15). `sense-1` is `input-magazine-counter` (7i84 input 16, inverted).
  - The component drives `output-tool-magazine-fwd` and `output-tool-magazine-rev`.
  - Debounce is 50 ms and home offset is 1. See `BPVMC_Toolchanger.hal`.
- **Where the logic lives:**
  - All former TNC PLC I/O is on named HAL signals in `BPVMC_IO.hal`. Each can be toggled from halshow; the `.halshow` watchlists in this folder are for that.
  - M6 is remapped to `toolchange.ngc` (see `[RS274NGC]`), which calls the subroutines in `atc_subroutines/` via M64/M65 outputs mapped in `BPVMC_Toolchanger.hal`.
  - Probing and tool setting use PSNG (`psng/`), customised for this ATC.

## Status
**Working:** X, Z and A; the spindle with encoder feedback and M19 orient; the probe; the manual magazine buttons; PSNG.

**Current task: the ATC subroutine set in `atc_subroutines/`.** A restructure is in progress and uncommitted:
- new `atc_req_*` subroutines, plus `atc_arm_run_to`, `atc_arm_reset`, `atc_arm_stop`, `atc_home` and `atc_step`
- new `atc_additions.hal`
- `atc_arm_rest` removed

**Outstanding:**
1. Carousel positioning is unreliable. Not yet diagnosed.
2. Tool holder up/down is unreliable. Cause unknown.
3. The Y axis hardware (see above).
4. Deferred: a once-per-rev error on the AEDL encoders from an off-centre code disc. It waits for the Hardinge lathe to be converted, which is needed to make a tapered adapter.
