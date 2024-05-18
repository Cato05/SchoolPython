import os

a = int(input("Adj egy számot: "))
l = []

l.append(a)

if l[0] % 3 == 0 and l[0] % 5 != 0:
    print("Osztható 3-mal.")
elif l[0] % 5 == 0 and l[0] % 3 != 0:
    print("Osztható 5-tel.")

if l[0] % 5 == 0 and l[0] % 3 == 0:
    print("Osztható 3-mal és öttel")