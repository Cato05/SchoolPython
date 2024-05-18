import os
import math

óra = (int(input("Kérem adja meg az órát: ")))

if óra <= 8 or óra < 16:
    (print("Nyitva"))
    niytva = 16-óra
    print("Még ",niytva, "óráig van nyitva a bolt.")
else:
    print("Zárva")