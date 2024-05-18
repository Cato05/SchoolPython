a = str(input("Van párhuzamos oldalpárja?"))

if a == "I":
    c = input("Két párhuzamos oldalpárja van?")
    if c == "I":
        d = input("Van derékszöge?")
        if d == "I":
            e = input("Oldalai egyenlők?")
            if e == "I":
                print("Négyzet")
            else:
                print("Téglalap")
        else:
            f = input("Oldalai egyenlők?")
            if f == "I":
                print("Rombusz")
            else:
                print("Paralelogramma")
    else:
        print("Trapéz")

    
else:
    b = str(input("Két-két szomszádos oldala egyenlő?"))
    if b == "I":
        print("Négyszög")
    else:
        print("Deltoid")