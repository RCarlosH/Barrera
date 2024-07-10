# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from servo import Servo
import time
from machine import Pin, I2C
import ssd1306

# Create network connection
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.poweron()
display.fill(0)
display.fill_rect(0, 0, 32, 32, 1)
display.fill_rect(2, 2, 28, 28, 0)
display.vline(9, 8, 22, 1)
display.vline(16, 2, 22, 1)
display.vline(23, 8, 22, 1)
display.fill_rect(26, 24, 2, 4, 1)
display.text('MicroPython', 40, 0, 1)
display.text('SSD1306', 40, 12, 1)
display.text('OLED 128x64', 40, 24, 1)
display.show()

# Test servos
motor=Servo(pin=13) # A changer selon la broche utilisée
motor.move(135)

while motor.current_angle > 90:
    motor.move(motor.current_angle - 2)
    time.sleep(0.02)
print(motor.current_angle)

while motor.current_angle < 180:
    motor.move(motor.current_angle + 2)
    time.sleep(0.02)
print(motor.current_angle)


# Blink LEDs


# Buzzer


# IR status on OLED + startup message


# Wait for a successful connection
import network
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('esp', '32323232')
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig()[0])

# Set OLED message
display.fill(0)
display.text('Connected', 0, 0)
display.text(sta_if.ifconfig()[0], 0, 10)
display.show()
