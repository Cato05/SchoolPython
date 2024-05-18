import os
import math

dic = {}

a = int(input("Adjad meg a pontszámot: "))

dic.update({"b" : a})

if int(dic.get("b")) >= 85:
    print("Ötös!")
elif int(dic.get("b")) <= 70 and int(dic.get("b")) < 85:
    print("Négyes.")
elif int(dic.get("b")) <= 60 and int(dic.get("b")) < 70:
    print("Hármás.")
elif int(dic.get("b")) <= 50 and int(dic.get("b")) < 60:
    print("Kettes.")
elif int(dic.get("b")) < 50:
    print("Megbuktál. Ja, egyes.")