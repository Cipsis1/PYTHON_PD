import random
miklas = {'Četras kājas, viena cepure':'Galds', 'Zelta puķe krāsnī zied':'Uguns', 'Siers jūras dibenā':'Saule', 'Plikpauris gaisā':'Mēness', 'Galva no dzelzs, kājas no koka':'Āmurs', 'Zoss ar četriem deguniem':'Spilvens', 'Mežā un mājā vienā vārdā':'Ieva', 'Nekad nesadeg, nekad nenoslīkst':'Ēna', 'Asiņu tēvs līkām kajām':'Ods', 'Otram rāda pats neredz':'Brilles'}

atslegas = list(miklas.keys())
skaits = 0
pareizas_atbildes = 0

def punktu_skaitisana(punkti):
    global pareizas_atbildes
    pareizas_atbildes += punkti

def randomMikla():
    return random.choice(atslegas)

print("Ja vēlies spēli beigt ievadi 'q'!")

while True:
    gadijums = randomMikla()
    minejums = input(f"{gadijums}: ")
    if skaits == 4:
        break
    elif minejums.lower() == "q":
        print("Paldies par spēli!")
        break
    elif pareizas_atbildes == 2 and pareizas_atbildes < 3:
        print("Trīs pēc kārtas!")
        punktu_skaitisana(1)
    elif minejums.capitalize() == miklas[gadijums]:
        print("Pareizi!")
        punktu_skaitisana(1)
    else:
        print("Nepareizi!")
    skaits +=1

print(f"Tu pareizi atbildēji uz {pareizas_atbildes} no {skaits + 1} jautājumiem!")
