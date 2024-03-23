import random
miklas = {'Četras kājas, viena cepure':'Galds', 'Zelta puķe krāsnī zied':'Uguns', 'Siers jūras dibenā':'Saule', 'Plikpauris gaisā':'Mēness', 'Galva no dzelzs, kājas no koka':'Āmurs'}

atslegas = list(miklas.keys())
skaits = 0
pareizas_atbildes = 0

def randomMikla():
    return random.choice(atslegas)

print("Ja vēlies spēli beigt ievadi 'q'!")

while True:
    gadijums = randomMikla()
    minejums = input(f"{gadijums}: ")
    if minejums.lower() == "q":
        print("Paldies par spēli!")
        break
    elif pareizas_atbildes == 2:
        print("Trīs pēc kārtas!")
    elif skaits == 4:
        break
    elif minejums.capitalize() == miklas[gadijums]:
        print("Pareizi!")
        pareizas_atbildes += 1
    else:
        print("Nepareizi!")
    skaits +=1

print(f"Tu pareizi atbildēji uz {pareizas_atbildes} no {skaits + 1} jautājumiem!")
