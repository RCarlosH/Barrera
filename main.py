# import libraries
import time
import network
from machine import Pin, PWM, I2C
from servo import Servo
import ssd1306

# Functions
def toggle_pin(pin):
    if pin.value() == 0:
        pin.value(1)
    else:
        pin.value(0)

# Pin assignment
pin_i2c_sda     = 04
pin_i2c_scl     = 05

pin_i_estopBtn = 06
pin_o_estopBtn = 07
pin_i_greenBtn = 09
pin_o_greenBtn = 10
pin_i_IR    = 11
pin_o_IR    = 12
pin_o_sevo1 = 13
pin_o_sevo2 = 14
pin_o_buzz  = 15

i2c         = I2C(sda=Pin(pin_i2c_sda), scl=Pin(pin_i2c_scl))
i_estopBtn  = Pin(pin_i_estopBtn,   Pin.IN, Pin.PULL_DOWN)
o_estopBtn  = Pin(pin_o_estopBtn,   Pin.OUT)
i_greenBtn  = Pin(pin_i_greenBtn,   Pin.IN, Pin.PULL_DOWN)
o_greenBtn  = Pin(pin_o_greenBtn,   Pin.OUT)
i_IR        = Pin(pin_i_IR,         Pin.IN, Pin.PULL_DOWN)
o_IR        = Pin(pin_o_IR,         Pin.OUT)
o_sevo1     = Servo(pin=pin_o_sevo1)
o_sevo2     = Servo(pin=pin_o_sevo2)
o_buzz      = Pin(pin_o_buzz,       Pin.OUT)
oled        = ssd1306.SSD1306_I2C(128, 64, i2c)

# Startup
## Variable setting
oled.poweron()
ticket_not_valid_blink_counter = 0
ticket_valid = 0 # 0: not read, 1: valid, 2: not valid
## Wifi config
while sta_if.isconnected == False:
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('esp', '32323232')
    time.sleep(2)

# Main func --------------------
# Estop behavior
tmr_estop_bh_start = time.ticks_ms()
while i_estopBtn.value() == 1:
    oled.fill(0)
    oled.text('E-Stop enabled', 0, 0)
    oled.show()
    # blink red LED
    tmr_estop_bh_loop = time.ticks_ms()
    if time.ticks_diff(tmr_estop_bh_loop, tmr_estop_bh_start) > 300:
        toggle_pin(o_estopBtn)
        tmr_estop_bh_start = time.ticks_ms()
    # Set status screen
o_estopBtn.off()

# Clear screen
oled.fill(0)
oled.show()

# Read NFC tag


# Query DB
ticket_valid = int(input('0/1/2: '))


# If ticket not valid
tmr_estop_bh_start = time.ticks_ms()
while ticket_valid == 2:
    # Show message on screen
    oled.fill(0)
    oled.text('Ticket not valid', 0, 0)
    oled.show()

    # Blink red LED
    tmr_estop_bh_loop = time.ticks_ms()
    if time.ticks_diff(tmr_estop_bh_loop, tmr_estop_bh_start) > 300:
        if ticket_not_valid_blink_counter < 4:
            toggle_pin(o_estopBtn)
            ticket_not_valid_blink_counter += 1
            tmr_estop_bh_start = time.ticks_ms()
        else:
            o_estopBtn.off()
            ticket_valid = 0
            oled.fill(0)
            oled.show()

    
# If valid
while ticket_valid == 1:
    # Show user name on OLED
    #oled.fill(0)
    #oled.show()

    # Turn on green LED
    o_greenBtn.value(1)

    # Open barrier
    o_sevo1.move(90)
    o_sevo2.move(90)

    # Register in DB

    # Delay
    time.sleep(2.5)

    # Wait for IR sensor to be 0

    # Delay
    time.sleep(0.5)

    # Close barrier
    o_sevo1.move(180)
    o_sevo2.move(0)
    # Clear OLED
    oled.fill(0)
    oled.show()

    # Resume normal operation
    ticket_valid = 0
    o_greenBtn.value(0)

