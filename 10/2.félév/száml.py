import random as r
sikeres = 0

for i in range(5):
    osztandó = r.randint(15, 20)
    osztó = r.randint(3, 7)
    maradék = osztandó % osztó

    válasz = int(input(f"Mennyi a(z) {osztandó} : {osztó} osztás maradéka? "))
    if válasz == maradék:
        print("Így van, ügyes vagy.")
        sikeres += 1
    else:
        print("Nincs igazad, a válasz: ",maradék)
print(sikeres)