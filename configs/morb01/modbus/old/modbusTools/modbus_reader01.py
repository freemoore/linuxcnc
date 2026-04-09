#!/usr/bin/env python3
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException

PORT = "/dev/ttyUSB0"
BAUD = 115200

# UM72/N4D3E16 typically supports 1..64 (some docs say 1..247, but 64 is common for these boards)
SLAVE_RANGE = range(1, 247)

# For UM72/N4D3E16, these are the most likely readable holding registers:
# 0: input bitfield (16 inputs)
# 1: output bitfield (16 outputs)
PROBE_REGS = (0, 1)

def is_ok(resp) -> bool:
    return resp is not None and hasattr(resp, "isError") and not resp.isError()

def main():
    client = ModbusSerialClient(
        port=PORT,
        baudrate=BAUD,
        parity="E",
        stopbits=1,
        bytesize=8,
        timeout=2,
    )

    if not client.connect():
        raise SystemExit(f"Failed to connect to {PORT} (permissions/wiring/adapter).")

    try:
        for sid in SLAVE_RANGE:
            client.slave_id = sid

            for reg in PROBE_REGS:
                try:
                    r = client.read_holding_registers(reg, 1)
                except ModbusException:
                    r = None
                except Exception:
                    r = None

                if is_ok(r):
                    val = r.registers[0]
                    print(f"FOUND device at slave ID {sid}")
                    print(f"Responded to FC03 holding reg {reg} -> 0x{val:04X} ({val})")
                    return

        print("No device responded.")
        print("If you're sure wiring is correct, try parity='E' and/or increase timeout to 1.0s.")

    finally:
        client.close()

if __name__ == "__main__":
    main()
