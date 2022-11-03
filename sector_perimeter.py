import math
while True:
    try:
        a, d = input("arc degrees,diameter").split(",")
        a = int(a)
        d = int(d)
        answer = (a/360)*d*math.pi+d
        print(f"({a}/360)*{d}*pi+{d} = {answer}")
    except:
        pass
