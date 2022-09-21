from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
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
splash = displayio.Group()
display.show(splash)

def findArea(p1, p2, p3):
    a = .5*(p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1]))
    return abs(a)

def inputToPoint(i):
    iSplit = i.split(",")
    p = (float(iSplit[0].replace(",","")), float(iSplit[1]))
    print(p)
    return p

xAxis = Line(0,32,128,32, color=0xFFFF00)
yAxis = Line(64, 0, 64, 128, color=0xFFFF00)

while True:
    while len(splash) > 0:
        splash.pop()
    try:
        point1 = inputToPoint(input("Input 1: "))
        point2 = inputToPoint(input("Input 2: "))
        point3 = inputToPoint(input("Input 3: "))
        area = findArea(point1, point2, point3)
        print(area)
        areaArea = label.Label(terminalio.FONT, text=f"area: {area}", color=0xFFFF00, x=0, y=0)
        splash.append(areaArea)
        splash.append(xAxis)
        splash.append(yAxis)
        triangle = Triangle(point1[0]-64, 32-point1[1], point2[0]-64, 32-point2[1], point3[0]-64, 32-point3[1], outline=0xFFFF00)
        splash.append(triangle)

    except:
        print("invalid input")
    if input("n to exit: ") == "n":
        exit()