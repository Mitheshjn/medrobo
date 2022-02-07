#!/usr/bin/env python3
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        ser.write(b"F")
        time.sleep(1)
        ser.write(b"S")
        time.sleep(1)
        ser.write(b"B")
        time.sleep(1)
        ser.write(b"S")
        time.sleep(1)
        ser.write(b"R")
        time.sleep(1)
        ser.write(b"S")
        time.sleep(1)
        ser.write(b"L")
        time.sleep(1)
        ser.write(b"S")
