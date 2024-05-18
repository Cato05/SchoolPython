import os

a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg egy számot: "))
c = int(input("Adj meg egy számot: "))

l = []
l.append(a)
l.append(b)
l.append(c)

if l[0] + l[1] == l[2]:
    print("Az első, és második szám összege, egyenlő a harmadikkal.")
elif l[0] + l[2] == l[1] :
    print("Az első, és harmadik szám összege, egyenlő a másodikkal.")
elif l[2] + l[0] == l[1]:
    print("A harmadik, és első szám összege, egyenlő a másodikkal.")