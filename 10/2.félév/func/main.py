import time
from time import sleep
from rich.console import Console


def maximumMinimum():
    a = int(input("Adj meg egy számot: "))

    b = int(input("Adj meg egy számot: "))

    c = int(input("Adj meg egy számot: "))


    print("A legnagyobb szám: ", max(a, b, c))
    print("A legkisebb szám: ", min(a, b, c))




def Különböz():
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

def Pontszám():
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


def oszthat():
    a = int(input("Adj egy számot: "))
    dic = {}

    dic.update({"b": a})

    if int(dic.get("b")) % 3 == 0 and int(dic.get("b")) % 5 != 0:
        print("Osztható 3-mal.")
    elif int(dic.get("b")) % 5 == 0 and int(dic.get("b")) % 3 != 0:
        print("Osztható 5-tel.")

    if int(dic.get("b")) % 5 == 0 and int(dic.get("b")) % 3 == 0:
        print("Osztható 3-mal és öttel")


def összead():
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
    else:
        print("Fogalmam sincs")



def páros():
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


def valami():
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

def hatványozás():
    while True:
        try:
            A = int(input("Adj meg egy valós számot: "))
            K = int(input("Adj meg egy egész számot: "))
            break
        except ValueError:
            print("Mondom egész!")

    dic = {}
    dic.update({"A": A})
    dic.update({"K": K})


    def pow(a,b):
        if(b==0):
            return 1
            
        answer=a
        increment=a
        
        for i in range(1,b):
            for j in range (1,a):
                answer+=increment
            increment=answer
        return answer
    
    
    print(pow(int(dic.get("A")), int(dic.get("K"))))

def átvált():
    x = int(input("Kérlek adj meg egy számot: "))
    rendszer = int(input("Kérlek add meg, hogy milyen számrendszerbe váltsam át: "))

    def tri(a):
        bit = []
        d = ""
        while a/rendszer != 0:
            b = a % rendszer
            if b == 10:
                d = str("A")
                bit.append(d)
                a = a//rendszer
            elif b == 11:
                d = str("B")
                bit.append(d)
                a = a//rendszer
            elif b == 12:
                d = str("C")
                bit.append(d)
                a = a//rendszer
            elif b == 13:
                d = str("D")
                bit.append(d)
                a = a//rendszer
            elif b == 14:
                d = str("E")
                bit.append(d)
                a = a//rendszer
            elif b == 15:
                d = str("F")
                bit.append(d)
                a = a//rendszer
            elif b == 16:
                d = str("G")
                bit.append(d)
                a = a//rendszer
            elif b == 17:
                d = str("H")
                bit.append(d)
                a = a//rendszer
            elif b == 18:
                d = str("I")
                bit.append(d)
                a = a//rendszer
            elif b == 19:
                d = str("J")
                bit.append(d)
                a = a//rendszer
            elif b == 20:
                d = str("K")
                bit.append(d)
                a = a//rendszer
            elif b == 21:
                d = str("L")
                bit.append(d)
                a = a//rendszer
            elif b == 22:
                d = str("M")
                bit.append(d)
                a = a//rendszer
            elif b == 23:
                d = str("N")
                bit.append(d)
                a = a//rendszer
            elif b == 24:
                d = str("O")
                bit.append(d)
                a = a//rendszer
            elif b == 25:
                d = str("P")
                bit.append(d)
                a = a//rendszer
            elif b == 26:
                d = str("Q")
                bit.append(d)
                a = a//rendszer
            elif b == 27:
                d = str("R")
                bit.append(d)
                a = a//rendszer
            elif b == 28:
                d = str("S")
                bit.append(d)
                a = a//rendszer
            elif b == 29:
                d = str("T")
                bit.append(d)
                a = a//rendszer
            else:    
                bit.append(b)
                a = a//rendszer

        print(bit[::-1])

    tri(x)


print("Lusta vagyok rendesen kiiratni.")
time.sleep(1)
print("Cserébe itt egy fasza töltőképernyő")
console = Console()
tasks = [f"{n}" for n in range(0, 4)]
j = ["Világ létrehozása...", "Kígyó megetetése...", "Finom az alma...", "Eleketromosság feltalálása...", "Gépek lázadása..."]

with console.status("[bold green]Loading...") as status:
    while tasks:
        task = int(tasks.pop(0))
        sleep(1)
        console.log(f"{j[task]} Kész")

a = int(input("Nyomj meg egy számot 1, és 9 között: "))

if a == 1:
    maximumMinimum()
elif a == 2:
    Különböz()
elif a == 3:
    Pontszám()
elif a == 4:
    oszthat()
elif a == 5:
    összead()
elif a == 6:
    páros()
elif a == 7:
    valami()
elif a == 8:
    hatványozás()
elif a == 9:
    átvált()