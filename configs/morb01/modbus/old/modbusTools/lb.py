import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
print("Port opened:", ser.name)

# Send test data
test_data = b'\x01\x03\x00\xFE\x00\x01\xE5\xFA'
print(f"Sending: {test_data.hex()}")
ser.write(test_data)

# Try to read it back
time.sleep(0.1)
if ser.in_waiting > 0:
    received = ser.read(ser.in_waiting)
    print(f"Received: {received.hex()}")
    print("✓ Loopback working!")
else:
    print("✗ No data received - loopback NOT working")

ser.close()
