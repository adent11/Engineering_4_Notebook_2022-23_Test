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

triList = [['-50,-17','-57,12','-22,-7'],['28,-14','60,-7','54,18'],['45,30','51,-1','18,6'],['5,5','19,15','22,10']]
cDists = []

def evaluateTriangle(p1, p2, p3):
    a = abs(.5*(p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])))
    c = ((p1[0] + p2[0] + p3[0])/3, (p1[1] + p2[1] + p3[1])/3)
    return [a, c]

def inputToPoint(i):
    iSplit = i.split(",")
    p = (float(iSplit[0].replace(",","")), float(iSplit[1]))
    print(p)
    return p

xAxis = Line(0,32,128,32, color=0xFFFF00)
yAxis = Line(64, 0, 64, 128, color=0xFFFF00)
triangle = Triangle(54, 26, 10, 13, 4, 62, outline=0xFFFF00) #Triangle(point1[0]+64, 32-point1[1], point2[0]+64, 32-point2[1], point3[0]+64, 32-point3[1], outline=0xFFFF00)

for tri in triList:
    tData = evaluateTriangle(tri)
    point1 = inputToPoint(tri[0])
    point2 = inputToPoint(tri[1])
    point3 = inputToPoint(tri[2])
    triData = evaluateTriangle(point1, point2, point3)



while True:
    while len(splash) > 0:
        splash.pop()
    try:
        point1 = inputToPoint(input("Input 1: "))
        point2 = inputToPoint(input("Input 2: "))
        point3 = inputToPoint(input("Input 3: "))
        area = findArea(point1, point2, point3)
        print(area)
        areaArea = label.Label(terminalio.FONT, text=f"area: {area}", color=0xFFFF00, x=0, y=4)
        triangle = Triangle(int(point1[0]+64), int(32-point1[1]), int(point2[0]+64), int(32-point2[1]), int(point3[0]+64), int(32-point3[1]), outline=0xFFFF00)
        splash.append(areaArea)
        splash.append(xAxis)
        splash.append(yAxis)
        splash.append(triangle)
        display.show(splash)

    except:
        print("invalid input")
    if input("n to exit: ") == "n":
        exit()