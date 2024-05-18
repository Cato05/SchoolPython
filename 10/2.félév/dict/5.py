import os

a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg egy számot: "))
c = int(input("Adj meg egy számot: "))

dic = {}
dic.update({"a": a})
dic.update({"b": b})
dic.update({"c": c})

if int(dic.get("a")) + int(dic.get("b")) == int(dic.get("c")):
    print("Az első, és második szám összege, egyenlő a harmadikkal.")
elif int(dic.get("a")) + int(dic.get("c")) == int(dic.get("b")) :
    print("Az első, és harmadik szám összege, egyenlő a másodikkal.")
elif int(dic.get("c")) + int(dic.get("a")) == int(dic.get("b")):
    print("A harmadik, és első szám összege, egyenlő a másodikkal.")