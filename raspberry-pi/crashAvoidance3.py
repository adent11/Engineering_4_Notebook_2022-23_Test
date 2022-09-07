import adafruit_mpu6050, busio, board, digitalio, terminalio, displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
sdaPin = board.GP14
sclPin = board.GP15
i2c = busio.I2C(sclPin, sdaPin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP19)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

while True:
    accel = mpu.acceleration
    led.value = accel[2] < 0