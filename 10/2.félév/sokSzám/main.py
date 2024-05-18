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