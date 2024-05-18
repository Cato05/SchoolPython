import os
import math

l = []

a = int(input("Adjad meg a pontszámot: "))

l.append(a)

if l[0] >= 85:
    print("Ötös!")
elif l[0] <= 70 and l[0] < 85:
    print("Négyes.")
elif l[0] <= 60 and l[0] < 70:
    print("Hármás.")
elif l[0] <= 50 and l[0] < 60:
    print("Kettes.")
elif l[0] < 50:
    print("Megbuktál. Ja, egyes.")