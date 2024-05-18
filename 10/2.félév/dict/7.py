y = 0
i = 0
while True:
    try:
        y = int(input("Adj meg egy pozitív egész számot: "))
        break
    except ValueError:
        print("Mondom egész!")

dic = {}
dic.update({"y":y})

if int(dic.get("y")) <= 0:
    print("Mondom pozitív!")
else:
    for x in range(1, int(dic.get("y")+1)):
        if x % 3 == 0:
            print(x)
        else:
            continue