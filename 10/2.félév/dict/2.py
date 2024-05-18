import os

a = int(input("Adj egy számot: "))
b = int(input("Adj egy számot: "))
c = int(input("Adj egy számot: "))

dic = {}

dic.update({"a" : a})
dic.update({"b" : b})
dic.update({"c" : c})

if int(dic.get("a")) != int(dic.get("b")) != int(dic.get("c")):
    print("Három különböző szám.")
else:
    print("Nem különbözőek")