from time import sleep
import board, digitalio
rLed = digitalio.DigitalInOut(board.GP17)
gLed = digitalio.DigitalInOut(board.GP16)
button = digitalio.DigitalInOut(board.GP15)
rLed.direction = digitalio.Direction.OUTPUT
gLed.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

print("File run")

lifted = False
while lifted == False:
    aborted = False
    while button.value == False:
        pass
    for i in range(10):
        print(10-i)
        rLed.value = True
        sleep(.1)
        rLed.value = False
        sleep(.9)
        if button.value == True:
            print("Operation Aborted.")
            sleep(.5)
            aborted = True
            break
    if not aborted:
        lifed = True
        gLed.value = True
        print("Liftoff.")


while True:
    pass