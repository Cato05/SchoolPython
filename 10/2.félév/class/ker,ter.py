import math



class sokszög:
    def __init__(self):
        a = int(input("Kélrek add meg egy oldal méretét: "))
        c = a
        b = 0
        while str(input("Szeretnél még oldalt megadni? (n/i): ")) == "i":
            a = int(input("Akkor hajrá: "))
            c = a + b

            b = a
        self.ker = c
    



s = sokszög()

print(s.ker)