import RPi.GPIO as gpio
import serial
import time
import sys
import os

def main():
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)

    s = serial.Serial('/dev/ttyACM0', 9600)
    status = False

    while 1:
        gpio.output(12, status)
        status = not status
        print status
        s.write("1\n" if status else "0\n")
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        gpio.cleanup()
        try:
            sys.exit(0)