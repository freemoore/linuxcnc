# Loopback test - write to output, then read it back

echo "=== Loopback Test ==="
echo "Writing 1 to output channel 1..."
mbpoll -a 1 -r 1 -t 4 -b 9600 -P none -1 /dev/ttyUSB0 1

sleep 0.5

echo "Reading back output channel 1..."
mbpoll -a 1 -r 1 -c 1 -t 3 -b 9600 -P none -1 /dev/ttyUSB0

echo ""
echo "Writing 0 to output channel 1..."
mbpoll -a 1 -r 1 -t 4 -b 9600 -P none -1 /dev/ttyUSB0 0

sleep 0.5

echo "Reading back output channel 1..."
mbpoll -a 1 -r 1 -c 1 -t 3 -b 9600 -P none -1 /dev/ttyUSB0
