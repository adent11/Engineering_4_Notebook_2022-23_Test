import adafruit_mpu6050, busio, board, digitalio, terminalio, displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from time import sleep
displayio.release_displays()
sdaPin = board.GP14
sclPin = board.GP15
i2c = busio.I2C(sclPin, sdaPin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP17)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

# create the display group
splash = displayio.Group()

# add title block to display group
title = "ANGULAR VELOCITY"
# the order of this command is (font, text, text color, and location)
title_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)

# you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
# Don’t forget to round the angular velocity values to three decimal places
count=0
# send display group to screen
display.show(splash)
while True:
    accel = mpu.acceleration
    led.value = accel[2] < 0
    x_area = label.Label(terminalio.FONT, text=f"x: {round(accel[0], 3)}", color=0xFFFF00, x=5, y=15)
    y_area = label.Label(terminalio.FONT, text=f"y: {round(accel[1], 3)}", color=0xFFFF00, x=5, y=25)
    z_area = label.Label(terminalio.FONT, text=f"z: {round(accel[2], 3)}", color=0xFFFF00, x=5, y=35)
    while len(splash) > 0:
        splash.pop()
    splash.append(title_area)
    splash.append(x_area)
    splash.append(y_area)
    splash.append(z_area)
    display.show(splash)
    sleep(.1)
    count = count + 1
    print(count)