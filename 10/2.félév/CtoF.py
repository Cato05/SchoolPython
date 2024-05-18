file = open("Temps.txt", "a")

def fc (c):
    f = float((c * 9/5) + 32)
    k = int(c),"C°", "\t", "====>", int(f),"F°"
    file.write(str(k))

def cf (f):
    c = float((f - 32) / 1.8)
    k = int(f),"F°", "\t", "====>","\t", int(c),"C°"
    file.write(str(k))

a = float(input("Adj meg egy fokot: "))
b = str(input("A megadott érték Celsius, vagy Fahren volt? (c/f): "))

if b == "c":
     fc(a)
else:
    cf(a)