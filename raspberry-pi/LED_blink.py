# type: ignore
from time import sleep
import board, digitalio
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT 

while True:
    led.value = True
    sleep(.2)
    led.value = False
    sleep(.2)