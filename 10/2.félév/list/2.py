import os

a = int(input("Adj egy számot: "))
b = int(input("Adj egy számot: "))
c = int(input("Adj egy számot: "))

l = []

l.append(a)
l.append(b)
l.append(c)

if l[0] != l[1] != l[2]:
    print("Három különböző szám.")
else:
    print("Nem különbözőek")