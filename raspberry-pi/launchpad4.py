from time import sleep
import board, digitalio
import pwmio
from adafruit_motor import servo

rLed = digitalio.DigitalInOut(board.GP17)
gLed = digitalio.DigitalInOut(board.GP16)
button = digitalio.DigitalInOut(board.GP15)
rLed.direction = digitalio.Direction.OUTPUT
gLed.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

def bound(x, min, max):
    if x > max:
        return max
    if x < min:
        return min
    return x

print("File run")
servo1.angle = 0

lifted = False
while lifted == False:
    while button.value == False:
        pass
    for i in range(10):
        print(10-i)
        if i > 6:
            servo1.angle = bound(180-(10-i)*45, 0, 180)
            print(f"turn to {bound(180-(10-i)*45, 0, 180)}")
        rLed.value = True
        sleep(.1)
        rLed.value = False
        sleep(1)
        
    lifed = True
    gLed.value = True
    print("Liftoff.")
    servo1.angle = 180


while True:
    pass