import os

a = int(input("Adj egy számot: "))
dic = {}

dic.update({"b": a})

if int(dic.get("b")) % 3 == 0 and int(dic.get("b")) % 5 != 0:
    print("Osztható 3-mal.")
elif int(dic.get("b")) % 5 == 0 and int(dic.get("b")) % 3 != 0:
    print("Osztható 5-tel.")

if int(dic.get("b")) % 5 == 0 and int(dic.get("b")) % 3 == 0:
    print("Osztható 3-mal és öttel")