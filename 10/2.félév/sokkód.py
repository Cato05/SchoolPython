a = int(input("Add meg a kezdő számot: "))
b = int(input("Add meg a végső számot: "))
osztható = int(input("Add meg, hogy mennyivel legyen osztható: "))


def szamok(a,b,oszt):
    if a % oszt == 0:
        tobbszorosok = list(range(a, b, oszt))
        sorok = list(tobbszorosok[i:i + 10] for i in range(0, len(tobbszorosok), 10))
        sorok_szovegkent = list(list(str(j) for j in i)for i in sorok)
        sorok_tabbal = list("\t".join(i) for i in sorok_szovegkent)
        return "\n".join(sorok_tabbal)
    else:
         a = a + (a % oszt)
         tobbszorosok = list(range(a, b, oszt))
         sorok = list(tobbszorosok[i:i + 10] for i in range(0, len(tobbszorosok), 10))
         sorok_szovegkent = list(list(str(j) for j in i)for i in sorok)
         sorok_tabbal = list("\t".join(i) for i in sorok_szovegkent)
         return "\n".join(sorok_tabbal)
    
megoldas = szamok(a,b,osztható)
with open("szamok.txt", "w") as file:
        file.write(megoldas)