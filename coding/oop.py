import random
"""
class Cat:
    # KONŠTRUKTOR
    def __init__(self, name, vek):
        self.name = name
        self.vek = vek
        print("Vytvaram objekt mačky")

    def __str__(self):
        print("Meno macky je ",  self.name)
        print("Vek macky je ", self.vek)
        return " "

    def mnau(self):
        print(self.name, " mňau")

    def zjedz(self, jedlo):
        print(self.name, " zjedlo")


cat = Cat("Cica", 3)


cat.mnau()
cat.zjedz("rybu")

cat2 = Cat("Murko", 5)
cat2.mnau()


class Auto:
    def __init__(self, znacka, rok_vyroby, farba, pocet_miest):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.farba = farba
        self.pocet_miest = pocet_miest
        self.nastartovane = False

    def __str__(self):
        print("Znacka je:", self.znacka, ", rok vyroby je:", self.rok_vyroby, ", farba je:", self.farba, ", pocet miest je:", self.pocet_miest, ", ze ci je nastartovane:", self.nastartovane)
        return " "

    def chod_dopredu(self):
        print("isiel som dopredu")

    def chod_dozadu(self):
        print("isiel som dozadu")

    def zatrub(self):
        print("Tutuuuuu")

    def ze_ci_je_nastartovane(self, nieco):
        self.nastartovane = nieco


print("auto1:")
auto1 = Auto("volvo", 2015, "siva", 6)
auto1.chod_dopredu()
auto1.zatrub()
auto1.ze_ci_je_nastartovane(False)
print(auto1)


print("auto2:")
auto2 = Auto("bmw", 2021, "cierna", 4)
auto2.chod_dozadu()
print(auto2)

class Kalulacka:
    def __init__(self):
        self.cislo1 = int(input("Číslo 1: "))
        self.cislo2 = int(input("Číslo 2: "))

    def __str__(self):
        return "Súčet: " + str(self.cislo1 + self.cislo2) + \
               "\nRozdiel: " + str(self.cislo1 - self.cislo2) + \
               "\nSúčin: " + str(self.cislo1 * self.cislo2) + \
               "\nPodiel: " + str(self.cislo1 / self.cislo2)





kalkulacka = Kalulacka()

print(kalkulacka)

import random


class NejakyObjekt:
    def __init__(self):
        self.pocet_hran = int(input("Počet hrán: "))

    def hod_kockou(self):
            print(random.randint(1, self.pocet_hran))

kocka1 = NejakyObjekt()
print("Kocka 1:")
for i in range(10):
    kocka1.hod_kockou()


kocka2 = NejakyObjekt()
print("Kocka 2:")
for x in range(10):
    kocka2.hod_kockou()


class Clovek:

    def __init__(self, meno, unava=0):
        self.unava = unava
        self.meno = meno
        
    def behat_1km(self):
        self.unava += 1
        
    def spat_1h(self):
        if self.unava >= 10:
            self.unava -= 10
        else:
            self.unava = 0

    def __str__(self):
        return f"{self.meno} {self.unava}"

clovek = Clovek("Marek")

for m in range(30):
    clovek.behat_1km()
    print(clovek)
    if clovek.unava == 20:
        print("som unaveny")
        nieco = input("chces spat? ")
        if nieco == "jj":
            clovek.spat_1h()
            continue
        if nieco == "nn":
            break



class RandomSentenceGenerator:


    def __init__(self):
        self.prid_m = ("dobrý", "veľký", "malý", "vysoký", "múdry")
        self.podst_m = ("Marek", "Jaro", "Kubo", "Timo", "Šimon", "Mário")
        self.prisl = ("pekne", "škaredo", "hlúpo", "rád", "odvážne")
        self.sloveso = ("programoval", "sa učil", "sa hral", "behal", "ťukal do klavesnice")
        self.miesto = ("doma", "vonku", "v škole", "na mesiaci", "v nočnom klube")



    def __str__(self):
        return f"{random.choice(self.prid_m)} {random.choice(self.podst_m)} {random.choice(self.prisl)} {random.choice(self.sloveso)} {random.choice(self.miesto)}"



rsg = RandomSentenceGenerator()
for i in range(10):
    print(rsg)
"""
nieco = ""
class Auto:
    def __init__(self, spz, farba):
        self.spz = spz
        self.farba = farba

    def zaparkuj(self):
        global nieco
        nieco = "zaparkovane"

auto1 = Auto("KM999BA", "sivá")
auto2 = Auto("ZA457HP", "s")
auto3 = Auto("CA540CH", "m")
auto1.zaparkuj()
auta = (auto1, auto2, auto3)

randomnieco = random.choice(auta)

x = []
if nieco != "":
    x.append(randomnieco.spz)


class Garaz:
    def __str__(self):
        return f"v garazi je auto {x[0]}"

garaz = Garaz()


print(garaz)























