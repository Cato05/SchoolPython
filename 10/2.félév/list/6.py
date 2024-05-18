a = int(input("Adj meg egy számot: "))

b = int(input("Adj meg egy számot: "))

c = int(input("Adj meg egy számot: "))

l = []
l.append(a)
l.append(b)
l.append(c)


if l[0] % 2 == 0 and l[1] % 2 == 0 and l[2] % 2 == 0:
    print("Mindegyik szám páros!")
else:
    print("Legalább az egyik szám páratlan.")