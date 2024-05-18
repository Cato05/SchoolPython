y = 0
i = 0
while True:
    try:
        y = int(input("Adj meg egy pozitív egész számot: "))
        break
    except ValueError:
        print("Mondom egész!")

l = []
l.append(y)

if l[0] <= 0:
    print("Mondom pozitív!")
else:
    for x in range(1, l[0]+1):
        if x % 3 == 0:
            print(x)
        else:
            continue