import os
import math

a = str(input("Kérem adja meg az első szót: "))
b = str(input("Kérem adja meg a második szót: "))

első = list(a)
második = list(b)

if első > második:
    print("Az első szó volt a hoszabb!")

elif első == második:
    print("A két szó egyenlő hosszúságú.")
else:
    print("A második szó volt a hoszabb!")
