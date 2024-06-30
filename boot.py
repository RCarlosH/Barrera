# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from servo import Servo
import time

# Create network connection


# Test servos
motor=Servo(pin=17) # A changer selon la broche utilisée
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


# Set OLED message
