from time import sleep
import board, digitalio
rLed = digitalio.DigitalInOut(board.GP17)
gLed = digitalio.DigitalInOut(board.GP16)
rLed.direction = digitalio.Direction.OUTPUT
gLed.direction = digitalio.Direction.OUTPUT

for i in range(10):
    print(10-i)
    rLed.value = True
    sleep(.1)
    rLed.value = False
    sleep(.9)
print("Liftoff.")
gLed.value = True

while True:
    pass