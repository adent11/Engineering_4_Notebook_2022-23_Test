import adafruit_mpu6050, busio, board
from time import sleep
sdaPin = board.GP14
sclPin = board.GP15
i2c = busio.I2C(sclPin, sdaPin)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    accel = mpu.acceleration
    print(f"X Acceleration: {accel[0]} \nY Acceleration: {accel[1]}\nZ Acceleration: {accel[2]}\n")
    sleep(.5)