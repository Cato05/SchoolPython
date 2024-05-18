a = int(input("Adjá' megfele egy számot: "))

dic = {}

dic.update({"a": a})

for i in range(0, int(dic.get("a"))):
    if i % 2 == 0:
        print("0")
    else:
        print(1)
    i += 1