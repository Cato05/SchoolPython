import random as r

csapat1_nev = str(input("Add meg az első csapat nevét: "))
csapat2_nev = str(input("Add meg a második csapat nevét: "))

csapat1_pont = r.randint(0, 12)
csapat2_pont = r.randint(0, 12)


if csapat1_pont > csapat2_pont:
    print(csapat1_nev, "nyert!", csapat1_pont, ":", csapat2_pont)
    if csapat1_pont - csapat2_pont >= 5:
        print("Ez biza nagy zakó volt")
    elif csapat2_pont > csapat1_pont: 
        print(csapat2_nev, "nyert!", csapat2_pont, ":", csapat1_pont)
        if csapat2_pont - csapat1_pont >= 5:
            print("Ez biza nagy zakó volt!")

if csapat1_pont == csapat2_pont:
    print("Error: Nem kezelhettem le ezt a lehetőséget!")