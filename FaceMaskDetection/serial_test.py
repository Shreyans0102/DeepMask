import serial
import time

arduino = serial.Serial('COM3', 9600, timeout = 0.1)
time.sleep(2)
arduino.write(b'1')
time.sleep(2)
arduino.write(b'2')