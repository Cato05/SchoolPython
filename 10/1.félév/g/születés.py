import os
import datetime

év = int(input("Kérem adja meg születési évszámát: "))
ja = bool(input("Kérem adja, meg, hogy volt-e már szülinapja ebben az évben (Írjon egy 1-est ha igen, 2-est, ha nem): "))

most = datetime.datetime.now()
kor = most.year - év - 1

if ja == 1:
    kor += 1

print("Ön", kor, "éves.")