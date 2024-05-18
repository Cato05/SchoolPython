data = open("epostak.txt", "rt")
file = open("results.txt", 'a')

l = []

for i in data:
    előző = str()
    k = data.readline()
    #spliteli a szöveget soronként
    é = (k.split('\t'))
    #Kiválasztja az elemet ahol az adatok vannak
    névElem = str(é[1])
    szolg = str(é[2])
    date = str(é[0])
    #Szétszedi a szóköz szerint
    év = date.split(".")
    név = névElem.split(' ')
    #Összerakja a Név elemeit
    check = név[0]+"."+név[1]
    if check == előző:
        név_összerak = év+név[0]+"."+név[1]+szolg
    else:
        név_összerak = név[0]+"."+név[1]+szolg
    előző = check
    print(név_összerak.lower())
    file.write(név_összerak.lower())