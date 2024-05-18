a = int(input("Adjá' megfele egy számot: "))

l = []

l.append(a)

for i in range(0, l[0]):
    if i % 2 == 0:
        print("0")
    else:
        print(1)
    i += 1