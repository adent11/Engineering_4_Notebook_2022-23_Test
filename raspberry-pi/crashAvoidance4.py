import adafruit_mpu6050, busio, board, digitalio, terminalio, displayio, adafruit_mpl3115a2
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
mpl = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)
mpl.sealevel_pressure = 102250
led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

# create the display group
splash = displayio.Group()
title_area = label.Label(terminalio.FONT, text="ANGULAR VELOCITY", color=0xFFFF00, x=5, y=5)
startAlt = mpl.altitude
while True:
    accel = mpu.acceleration
    led.value = accel[2] < 0 and mpl.altitude > startAlt + 3
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