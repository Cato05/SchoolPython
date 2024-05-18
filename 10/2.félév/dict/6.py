a = int(input("Adj meg egy számot: "))

b = int(input("Adj meg egy számot: "))

c = int(input("Adj meg egy számot: "))

dic = {}
dic.update({"a": a})
dic.update({"b": b})
dic.update({"c": c})


if int(dic.get("a")) % 2 == 0 and int(dic.get("b")) % 2 == 0 and int(dic.get("c")) % 2 == 0:
    print("Mindegyik szám páros!")
else:
    print("Legalább az egyik szám páratlan.")