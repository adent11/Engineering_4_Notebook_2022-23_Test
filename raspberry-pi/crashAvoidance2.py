import adafruit_mpu6050, busio, board, digitalio
from time import sleep
sdaPin = board.GP14
sclPin = board.GP15
i2c = busio.I2C(sclPin, sdaPin)
mpu = adafruit_mpu6050.MPU6050(i2c)
led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

while True:
    accel = mpu.acceleration
    led.value = accel[2] < 0