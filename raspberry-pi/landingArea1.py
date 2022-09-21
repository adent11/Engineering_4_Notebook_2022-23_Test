def findArea(p1, p2, p3):
    a = .5*(p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1]))
    return abs(a)

def inputToPoint(i):
    iSplit = i.split(",")
    p = (float(iSplit[0].replace(",","")), float(iSplit[1]))
    print(p)
    return p

while True:
    try:
        point1 = inputToPoint(input("Input 1: "))
        point2 = inputToPoint(input("Input 2: "))
        point3 = inputToPoint(input("Input 3: "))
        area = findArea(point1, point2, point3)
        print(area)
    except:
        print("invalid input")
    if input("n to exit: ") == "n":
        exit()