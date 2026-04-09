#!/usr/bin/env python3
import inspect
import pymodbus
from pymodbus.client import ModbusSerialClient

PORT = "/dev/ttyUSB0"
BAUD = 9600
TIMEOUT = 1.0

# UM72/N4D3E16 often uses 1..64, but scanning wider costs little.
SLAVE_RANGE = range(1, 65)

# Probe a few likely addresses (different clones/maps exist).
PROBE_ADDRS = [0, 1, 2, 10, 16, 100, 254, 255]

def _sig_str(fn):
    try:
        return str(inspect.signature(fn))
    except Exception:
        return "<signature unavailable>"

def _call_read(fn, address, count=1):
    """
    Call a pymodbus read_* function in a way that matches its signature.
    Tries:
      - keyword-only count (count=)
      - positional count
      - address only
    """
    sig = None
    try:
        sig = inspect.signature(fn)
        params = sig.parameters
        # Build kwargs only if accepted
        kwargs = {}
        if "address" in params:
            kwargs["address"] = address
            # count may be keyword-only or optional
            if "count" in params:
                kwargs["count"] = count
            return fn(**kwargs)

        # If no named params, fall back to positional strategies
    except Exception:
        pass

    # Fallback attempts (in decreasing “verbosity”)
    try:
        return fn(address, count)
    except TypeError:
        try:
            return fn(address, count=count)
        except TypeError:
            return fn(address)

def _set_slave(client, sid):
    """
    Set target slave in whatever way this pymodbus/client supports.
    Returns True if it managed to set it, False otherwise.
    """
    # Method forms
    if hasattr(client, "set_slave") and callable(getattr(client, "set_slave")):
        try:
            client.set_slave(sid)
            return True
        except Exception:
            pass

    # Attribute form
    if hasattr(client, "slave_id"):
        try:
            client.slave_id = sid
            return True
        except Exception:
            pass

    # Some variants accept slave/unit per call; handled elsewhere
    return False

def _try_per_call_slave(fn, sid):
    """
    Wrap a read function to inject slave/unit keyword if supported.
    """
    try:
        sig = inspect.signature(fn)
        params = sig.parameters
        if "slave" in params:
            return lambda **kw: fn(slave=sid, **kw)
        if "unit" in params:
            return lambda **kw: fn(unit=sid, **kw)
    except Exception:
        pass
    return None

def _ok(resp):
    return resp is not None and hasattr(resp, "isError") and not resp.isError()

def main():
    print(f"pymodbus version: {getattr(pymodbus, '__version__', 'unknown')}")

    client = ModbusSerialClient(
        port=PORT,
        baudrate=BAUD,
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=TIMEOUT,
    )

    # Show what this install actually exposes
    print(f"read_holding_registers signature: {_sig_str(client.read_holding_registers)}")
