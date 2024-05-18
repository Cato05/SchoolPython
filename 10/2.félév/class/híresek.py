class HíresNő:
    def __init__(self, név, foglalkozás, nemzet):
        self.név = név
        self.foglalkozás = foglalkozás
        self.nemzet = nemzet

    def előtag(self):
        if self.nemzet == 'a':
            return 'Ms.'
        else:
            return 'Frau'
        

nők = []


for i in range(0, 3):
    name = str(input("Add meg a nevet: "))
    job = str(input("Add meg a foglalkozását: "))
    country = str(input("Add meg a nemzetiségét (a/n): "))
    nő = HíresNő(name, job, country)
    nők.append(nő)



for nő in nők:
    print(nő.előtag(), nő.név, 'egy híres', nő.foglalkozás)