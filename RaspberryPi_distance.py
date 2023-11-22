# Run on the RaspberryPi(Client)
## 2023.06 / AI Age Estimation Kiosk

import time
import board
import busio
import digitalio
import socket

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

import RPi.GPIO as GPIO
import time

print("AkibaTV HC-SR04 Start")

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

# OLED setup
oled_reset = digitalio.DigitalInOut(board.D4)
WIDTH = 128
HEIGHT = 64
BORDER = 5

LOOPTIME = 1.0

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

oled.fill(0)
oled.show()

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Server configuration
HOST = '172.20.10.3'
PORT = 65000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    come_sent = False

    while True:
        try:
            draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
            GPIO.output(17, False)
            time.sleep(2)

            GPIO.output(17, True)
            time.sleep(1)
            GPIO.output(17, False)

            while GPIO.input(18) == 0:
                start = time.time()

            while GPIO.input(18) == 1:
                stop = time.time()

            time_interval = stop - start
            distance = time_interval * 17000
            distance = round(distance, 2)

            print("Distance => ", distance, "cm")

            # Check the measured distance and update the display and communication accordingly 
            if distance > 40:
                draw.text((50, 25), "EMPTY", fill="white")
                come_sent = False
            elif distance <= 40 and distance > 30:
                draw.text((50, 25), "Come", fill="white")
            
                # If the measured distance is "COME", send message to the server
                if not come_sent:
                    s.sendall(b'Come')
                    come_sent = True
            else:
                draw.text((50, 25), "USING", fill="white")
                come_sent = False

            oled.image(image)
            oled.show()
            time.sleep(LOOPTIME)

        except KeyboardInterrupt:
            GPIO.cleanup()
            print("AkibaTV HC-SR04 End")
            s.close()
