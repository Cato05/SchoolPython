import math as m

d = int(input("A fatörzs átmérője (cm) = "))
h = int(input("A fatörzs hossza (cm) = "))

p = 22/7

r = d/2
v = (r**2 * p * h) / 1000

print("A fatörzs térfogata = ", v, "m3.")