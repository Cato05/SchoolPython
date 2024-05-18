file = open("Temps.txt", "a")

def fc (c):
    c = c* (9/5)
    f = float(c + 32)
    é = "F°"
    k = str(c) + "C°" + "\t" + "====>" + "\t" + str(f) + str(é)
    file.write(k)

def cf (f):
    c = float((f - 32) / 1.8)
    at = (str(f),"F°", "\t" + "====>","\t", str(c) + "C°")
    k = "".join(at)

    file.write(k)

a = float(input("Adj meg egy fokot: "))
b = str(input("A megadott érték Celsius, vagy Fahren volt? (c/f): "))

if b == "c":
     fc(a)
else:
    cf(a)