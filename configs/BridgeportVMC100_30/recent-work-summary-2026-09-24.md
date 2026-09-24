# Bridgeport VMC1000-30: LinuxCNC retrofit status

**Author:** Claude (Cowork), for Andy Moore / TTTF. Written 24/09/2026 and corrected by Andy the same day.
**Purpose:** a handoff for Claude Code, which has direct access to the machine and its config.

> **Source caveat. Read this first.** This file comes from Claude's saved notes on what Andy said. It was not built from the config files or from full chat transcripts. So:
> - The numbers below (MP values, scales, gains, part numbers) are what Andy stated. **Check them against the live INI/HAL files, and flag any mismatch instead of "fixing" it.**
> - Debugging steps and dead ends that were never recorded are missing. Treat the outstanding list as a minimum.

---

## Machine
- Bridgeport VMC1000-30, 4,400 kg. The original control was a Heidenhain TNC407. It has a 30-tool ATC and a Nikken CNC-201 4th axis (A).
- **Control hardware:** Mesa 7i97T + 7i74 + 7i84U running LinuxCNC. The config was adapted from the working Morbidelli setup (Yaskawa SGDB drives).
- **Axis drives:** Siemens Simodrive 611 with analogue interface. The feed module control card is 6SN1118-0AA11-0AA1 (single-axis boards).
- **Axis motors:** Siemens 1FT5066-0AC71, rated 2000 rpm, max 3200 rpm. Each motor has an integrated 1FU brushless tacho (R/S/T/Mp) and a 3-channel rotor position sensor, both wired to the drive on X311. The motors can't be uncoupled from their axes, except Y at the moment (see below).
- **A axis drive:** Control Techniques Midi Maestro 140x14/28. This is separate from the 611 system.
- **Spindle:** Simodrive 611 80A power module (6SN1123-1AA00-0DA0) with control card 6SN1121-0BA11-0AA1 (the card with the +/P/- buttons). The spindle motor is 3-phase with analogue control.
- As far as Andy knows, no linear scales are fitted.

## Encoders
- The original Heidenhain ROD 350.005 encoders (500-line sin/cos, 9-pin plug) were replaced with **AEDL differential quadrature encoders with 5000-line code wheels, giving 20000 counts/rev**. The Mesa rig reads them correctly.
- The hostmot2 encoder filter is **off** for these 5000-line encoders, following PCW's advice.
- Original TNC407 MP values, for reference: MP330.0/.1 = 32, MP330.2 = 20, MP340.0–.4 = 0, MP1010.0 = 32000, MP1050.0 = 9, MP1060.0 = 3, MP1010.2 = 20000, MP1050.2 = 9, MP1060.2 = 3.

## Simodrive 611 wiring as used
- Setpoint is on 56/14. Pulse enable is 663. Controller enable is 65. NE infeed is 63/64/48. All are referenced to 9 (+24 V) and 19 (0 V).
- On X331 the only connections are 663 and 65 (red/blue pair). 663 is **strapped to 9, so pulse enable is always asserted**. X341 has 289, 296, 673 and 674 wired out.
- The 7i97T analogue enable is tied to the machine's original X/Y/Z enable signals.
- The spindle setpoint is on **7i97T analogue channel 5**.

## Axis config values (as stated)
| Axis | Stated values |
|---|---|
| Z | 10 mm lead ballscrew. ENCODER_SCALE −2000 gives the correct direction. P 200, FF2 0.004, OUTPUT_SCALE 370.4. Tuned and running at full rapid. Brake confirmed releasing on enable |
| A | 20000 counts per motor rev. ENCODER_SCALE −5000 counts/degree gives the correct jog direction. The ERO 115-100 originally fitted has been replaced |
| X | Working, and homing is workable. No tuning values recorded |
| Y | **Not running.** See the outstanding list |

- **Homing** uses no switches: HOME_SEARCH_VEL = 0, HOME_LATCH_VEL = 0, HOME_USE_INDEX = 0. It is workable on X and Z.

## Spindle
- This is the 6000 rpm build, with a single gear range. The TNC MP sheet (ETS273 p15) gives:
  - MP3210.0 = 9.9 V at MP3510.0 = 6000 rpm
  - MP3515.0 = 6000 max
  - MP3240.1 = 0.066 V min, which is a floor of about 40 rpm
  - .1–.7 are all zero
- Simodrive parameters: P-174 = P-029 = 9000 motor rpm, P-024 = 10 V, P-014.1 = 8140. The others are at the 9000 default.
- There is a visible belt reduction between motor and spindle. The implied ratio is about 1.343:1. This is **inferred, not measured**, so confirm it against the spindle encoder.
- **The spindle encoder is wired and working. M19 orient works.**

## ATC and PLC I/O
- The ATC is a SIDEPAL HL-20 double arm:
  - round 30-pocket carousel with a twin-gripper swing arm
  - the arm drops pneumatically
  - the arm rotates through a geneva cam driven by a motor with a brake override ("ambo")
- Relays: magazine fwd/rev, tool unclamp, tool holder up/down, air blast, arm motor, arm motor brake override.
- Magazine position is sensed by hall sensors over a steel codewheel: one index sensor plus a per-pocket counter. The original TNC drove the magazine in both directions.
- The TNC PLC I/O is all on X41/X42 (O0–O30, I0–I31). X47 is capped and no PL expansion board is fitted.
- **All PLC I/O has been moved to named HAL signals on Mesa I/O**, using `output-*` / `input-*` names (e.g. `output-tlmagdir`, `output-tlmagmove`, `input-store_orig`, `input-mag_counter`, `input-tla-rest`, `input-tla-r-pos`, `input-tla-f-pos`). Each signal can be toggled from halshow while the config is being built.
- Tool change uses PSNG, customised for this ATC.

## Status (24/09/2026)
**Working:**
- X, Z and A axes
- spindle, with encoder feedback and M19 orient
- probe
- the manual magazine buttons
- PSNG (ATC-customised)

**Outstanding:**
1. **The Y axis is down.** The Y motor is uncoupled and clamped to the bench:
   - no encoder is fitted, and the tacho hasn't been touched
   - the commutation cup and hall rig are attached
   - the rotor position sensor is a Siemens 2AV63 7315 (100 mm dia, hall-based) with a pressed-steel cup on the shaft
   - the sensor board can only be clocked about 10° mechanical in total

   The next step is either to repair the hall sensor or to couple a replacement motor. That decision is Andy's.
2. **Carousel positioning is unreliable.** These are suggested places to look first. None of them has been diagnosed:
   - counting of `input-mag_counter` edges, including debounce
   - the logic when the magazine changes direction
   - index resync against `input-store_orig`
3. **Tool holder up/down is unreliable.** The cause isn't recorded.
4. **Once-per-rev error on the AEDL encoders (deferred).** This is put down to the code disc being slightly off-centre. The fix is a 1:10 tapered-shaft adapter, which waits until the Hardinge lathe is in the new workshop and converted to LinuxCNC. Code doesn't need to act on this now.

## Suggested first moves (suggestions only)
- Read the current INI/HAL and compare it with the values above. Report differences to Andy.
- To see what the magazine is doing, run halscope on `input-mag_counter`, the index input and the direction/move outputs during a multi-pocket move in each direction.
- Keep Y disabled in any test config until the hardware decision is made.
