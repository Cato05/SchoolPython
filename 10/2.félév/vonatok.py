irány = str(input("Baracskára, vagy Pettendre ment a vonat (b/p)?: "))
if irány != "":
    kocsi = int(input("Hány kocsiból áll a szerelvény?: "))

    irá = []
    ko = []

    össz = 0

    while irány != "" and len(irá) != 99:
        irány = str(input("Baracskára, vagy Pettendre ment a vonat (b/p)?: "))
        if irány != "":
            kocsi = int(input("Hány kocsiból áll a szerelvény?: "))
            irá.append(irány)
            ko.append(kocsi)


    for i in range(0, len(ko)):
        össz = össz + ko[i]

    átlag = össz / len(ko)
    print("Átlagosan", átlag, "szerelvény haladt el.")