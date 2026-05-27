import time
import random
def main():
    while True:
        print(" ")
        print("---=== KASINO ===---")
        print(" ")
        print("Tervetuloa kasinolle!")
        print(" ")
        print("Pelivalikko")
        print("1. Ruletti")
        print(" ")
        print("2. Tower")
        print(" ")
#        print("3. Blackjack")
#        print(" ")
        print("3. Coinflip")
        print(" ")
        print("4. pelihistoria")
        print(" ")
        while True:
            pelivalinta = input("Valitse peli: ")
            if pelivalinta in ["1", "2", "3", "4"]:
                break
            print("Tätä peliä ei löytynyt🤔")
            time.sleep(1)
        if pelivalinta == "1":
            print(" ")
            print("---=== RULETTI ===---")
            print(" ")
            print("Rulettipöytä:")
            print(" ")
            print("0 (vihreä) 🟢")
            print("PUNAISET NUMEROT 🟥")
            print(" 1  3  5  7  9  12 14 16 18")
            print(" 19 21 23 25 27 30 32 34 36")
            print("MUSTAT NUMEROT ⬛")
            print(" 2  4  6  8  10 11 13 15 17")
            print(" 20 22 24 26 28 29 31 33 35")
            print(" ")
            print("Säännöt:")
            print(" ")
            print("🎡 Miten peli toimii?")
            print("1. Pelaaja valitsee, mihin haluaa panostaa")
            print("2. Pelaaja asettaa panoksen")
            print("3. Rulettipyörä arpoo numeron väliltä 0-36")
            print("4. Voitot maksetaan oikein arvattujen tulosten mukaan")
            print(" ")
            print("Panostus mahdollisuuudet:")
            print(" ")
            print("1. Valitse väri (punainen🟥/musta⬛) - voittokerroin 2")
            print("2. Valitse parillinen vai pariton - voittokerroin 2")
            print("3. Valitse alue (0-18 vai 19-36) - voittokerroin 2")
            print("4. Valitse numero (0-36) - voittokerroin 35")
            print("5. Valitse rivi (1-3) - voittokerroin 3")
            print(" ")
            print("Minimi panos: 1")
            print("Maksimi panos: 999999")
            print(" ")
            ruletti()
        elif pelivalinta == "2":
            print(" ")
            print("---=== TOWER ===---")
            print(" ")
            print("Säännöt: ")
            print(" ")
            print("🗼 Miten peli toimii?")
            print("1. Pelaaja asettaa panoksen")
            print("2. Jokaisessa kerroksessa on 3 laattaa")
            print("3. Yksi laatoista sisältää pommin 💣")
            print("4. Valitse turvallinen laatta jatkaaksesi")
            print("5. Jokainen kerros kasvattaa kerrointa")
            print("6. Voit cashoutata milloin tahansa")
            print("7. Jos osut pommiin, häviät kuitenkin kaiken mitä olet voittanut sekä panoksesi")
            print(" ")
            print("Kertoimet:")
            print("Kerros 1 = x2")
            print("Kerros 2 = x4")
            print("Kerros 3 = x8")
            print("Kerros 4 = x16")
            print("Kerros 5 = x32")
            print(" ")
            print("Minimi panos: 1")
            print("Maksimi panos: 999999")
            print(" ")
            tower()
        #elif pelivalinta == "3":
            #print("---=== BLACKJACK ===---")
            #print("In maintance")
            #blackjack()
        elif pelivalinta == "3":
            print(" ")
            print("---=== COINFLIP ===---")
            print(" ")
            print("Säännöt:")
            print(" ")
            print("🪙  Miten peli toimii?")
            print("1. Pelaaja asettaa panoksen")
            print("2. Pelaaja valitsee Kruuna tai Klaava")
            print("3. Kolikko heitetään")
            print("4. Jos arvaus osuu oikein, voitat")
            print("5. Jos arvaus menee väärin, häviät panoksen")
            print(" ")
            print("Voittokerroin: x2")
            print(" ")
            print("Minimi panos: 1")
            print("Maksimi panos: 999999")
            print(" ")
            coinflip()
        elif pelivalinta == "4":
            print(" ")
            print("---=== PELIHISTORIA ===---")
            print(" ")
            try:
                with open("pelihistoria.txt") as tiedosto:
                    sisalto = tiedosto.read()
                    print(sisalto)
            except FileNotFoundError:
                print("Pelihistoriaa ei vielä ole :(")
                time.sleep(1.5)
            
def tallenna(peli, tila, summa):
    teksti = f"{peli} | {tila} | {summa}€"
    with open("pelihistoria.txt", "a") as tiedosto:
        tiedosto.write(teksti + "\n")
    print("Tallennettu:", teksti)
            
def rulettivoitto():
    print("🟩🟩🟩🟩🟩🟩🟩🟩")
    print(f"🟩   Voitit!  🟩")
    print("🟩🟩🟩🟩🟩🟩🟩🟩")
    
def rulettihavio():
    print("🟥🟥🟥🟥🟥🟥🟥🟥")
    print(f"🟥  Hävisit...🟥")
    print("🟥🟥🟥🟥🟥🟥🟥🟥")

def rulettipyora():
    tulos = random.randint(0, 36)
    return tulos

def tekstitarkistus(kysymys, vastaukset): #tarkistus perkele 2.0
    while True:
        vastaus = input(kysymys).strip().lower()
        if vastaus in vastaukset:
            return vastaus
        print(" ")
        print("Virheellinen syöte!")
        print(f"Sallitut: {", ".join(vastaukset)}")
        print(" ")
        time.sleep(1)

def tarkistus(teksti, minimibet, maksimibet): #tarkistus perkele
    while True:
        try:
            numero = int(input(teksti))
            if numero < minimibet or numero > maksimibet:
                print(f"Anna numero väliltä {minimibet}-{maksimibet}")
                time.sleep(1)
                continue
            return numero
        except ValueError:
            print("Virheellinen syöte!")
            time.sleep(1)
            
def tarkistapanos(panos, saldo):
    while panos > saldo:
        print("Et voi panostaa enempää kuin saldosi")
        panos = tarkistus("Anna uusi panos: ", 1, 999999)
    return panos
    

def ruletti():
    saldo = tarkistus("Kuinka paljon saldoa sinulla on? ", 1, 999999)
    print("saldo", saldo, "€")
    print(" ")
    print("Miten haluat panostaa?")
    print(" ")
    while True:
        tapa = input("1. Väri, 2. Parillinen/Pariton, 3. Alue1 (0-18) - Alue2 (19-36), 4. numero, 5. rivit: ")
        if tapa in ["1", "2", "3", "4", "5"]:
            break
        print("Virheellinen panostustapa!")
        time.sleep(1)
    
    if tapa == "1":
        vari = tekstitarkistus("Valitse väri (punainen🟥/musta⬛): ", ["punainen", "musta"])
    elif tapa == "2":
        parillinen_pariton = tekstitarkistus("Valitse parillinen vai pariton: ", ["parillinen", "pariton"])
    elif tapa == "3":
        alue = tarkistus("Valitse alue, 1 (0-18) vai 2 (19-36): ", 1, 2)
    elif tapa == "4":
        numero = tarkistus("Valitse numero (0-36): ", 0, 36)
    elif tapa == "5":
        rivi = tarkistus("Valitse rivi (1-3): ", 1, 3)
   
    print(" ")    
    panos = tarkistus("Kuinka paljon haluat panostaa? ", 1, 999999)
    panos = tarkistapanos(panos, saldo)
    if panos == saldo:
            print("Vau! All in :D!")
    
    tulos = rulettipyora()
    punanen = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    musta = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    parillinen = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    pariton = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    alue1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    alue2 = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    rivi1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    rivi2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    rivi3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    print(" ")
    print("Rulettipyörä pyörii...")
    for i in range(3):
        print("Pyörii" + "." * (i+1))
        time.sleep(1.5)
    for i in range(3):
        print(" ")
    print("Ruletti pyörähti numeroon", tulos)
    print(" ")
    

    if tapa == "1":
        if vari == "punainen" and tulos in punanen:
            print("Tulos on punainen!")
            rulettivoitto()
            saldo += panos
            tallenna("RULETTI", "VOITTO", panos)
        elif vari == "musta" and tulos in musta:
            print("Tulos on musta!")
            rulettivoitto()
            saldo += panos
            tallenna("RULETTI", "VOITTO", panos)
        else:
            if tulos in punanen:
                print("Tulos on punainen!")
            elif tulos in musta:
                print("Tulos on musta!")
            rulettihavio()
            saldo -= panos
            tallenna("RULETTI", "HÄVIÖ", -panos)
        
        
    elif tapa == "2":
        if parillinen_pariton == "parillinen" and tulos in parillinen:
            print("Tulos on parillinen!")
            rulettivoitto()
            saldo += panos
            tallenna("RULETTI", "VOITTO", panos)
        elif parillinen_pariton == "pariton" and tulos in pariton:
            print("Tulos on pariton!")
            rulettivoitto()
            saldo += panos
            tallenna("RULETTI", "VOITTO", panos)
        else:
            rulettihavio()
            saldo -= panos
            tallenna("RULETTI", "HÄVIÖ", -panos)
        
        
    elif tapa == "3":
        if alue == 1 and tulos in alue1:
            print("Arvasit alueen 1, (0-18)")
            rulettivoitto()
            saldo += panos
            tallenna("RULETTI", "VOITTO", panos)
        elif alue == 2 and tulos in alue2:
            print("Arvasit alueen 2, (19-36)")
            rulettivoitto()
            saldo += panos
            tallenna("RULETTI", "VOITTO", panos)
        else:
            print(tulos, " ei ole alueella: ", alue)
            rulettihavio()
            saldo -= panos
            tallenna("RULETTI", "HÄVIÖ", -panos)

    elif tapa == "4":
        if numero == tulos:
            rulettivoitto()
            voitto = panos * 35
            saldo += voitto
            tallenna("RULETTI", "VOITTO", voitto)
        else:
            rulettihavio()
            saldo -= panos
            tallenna("RULETTI", "HÄVIÖ", -panos)

        
    elif tapa == "5":
        if rivi == 1 and tulos in rivi1:
            print("Tulos on rivillä 1!")
            rulettivoitto()
            voitto = panos * 3
            saldo += voitto
            tallenna("RULETTI", "VOITTO", voitto)
        elif rivi == 2 and tulos in rivi2:
            print("Tulos on rivillä 2!")
            rulettivoitto()
            voitto = panos * 3
            saldo += voitto
            tallenna("RULETTI", "VOITTO", voitto)
        elif rivi == 3 and tulos in rivi3:
            print("Tulos on rivillä 3!")
            rulettivoitto()
            voitto = panos * 3
            saldo += voitto
            tallenna("RULETTI", "VOITTO", voitto)
        else:
            print("Tulos ei ole rivillä ", rivi)
            rulettihavio()
            saldo -= panos
            tallenna("RULETTI", "HÄVIÖ", -panos)
            
    print("")
    print("Saldo tällä hetkellä:", saldo)
    print(" ")

def tower():
    saldo = tarkistus("Kuinka paljon saldoa sinulla on? ", 1, 999999)
    print("saldo", saldo, "€")
    print(" ")
    panos = tarkistus("Kuinka paljon haluat panostaa? ", 1, 999999)
    panos = tarkistapanos(panos, saldo)
    if panos == saldo:
            print("Vau! All in :D!")
    for i in range(3):
        print("Ladataan peliä" + "." * (i+1))
        time.sleep(1.5)
        
    kerroin = 1
    kerros = 1
    while kerros <= 5:
        print(" ")
        print("---=== TOWER ===---")
        print("Kerros 5, kerroin:", "32x")
        print(" "*5,"⬜⬜⬜")
        print("Kerros 4, kerroin:", "16x")
        print(" "*5,"⬜⬜⬜")
        print("Kerros 3, kerroin:", "8x")
        print(" "*5,"⬜⬜⬜")
        print("Kerros 2, kerroin:", "4x")
        print(" "*5,"⬜⬜⬜")
        print("Kerros 1, kerroin:", "2x")
        print(" "*5,"⬜⬜⬜")
        print("Kerros: ", kerros)
        print("Saldo: ", panos * kerroin, "€")
        pommi = random.randint(1, 3)
        valinta = tarkistus("Valitse laatta (1-3): ", 1, 3)
        print(" ")

        if valinta == pommi:
            print("🟥🟥🟥🟥🟥🟥🟥🟥")
            print("Hävisit! Peli ohi!")
            print("🟥🟥🟥🟥🟥🟥🟥🟥")
            saldo -= panos
            tallenna("TOWER", "HÄVIÖ", -panos)
            print("Saldo tällä hetkellä:", saldo)
            return
        else:
            print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")
            print("Turvallinen laatta! Voit jatkaa!")
            print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")
            kerroin *= 2
            kokonais = panos * kerroin
            voitto = kokonais - panos
            print("kerros: ", kerros+1)
            print("Saldo: ", kokonais, "€")
            print("Voitto: ", voitto, "€")
            while kerros <= 5:
                print(" ")
                jatka = input("Haluatko jatkaa? (k/e): ").lower()
                if jatka == "e":
                    saldo += voitto
                    tallenna("TOWER", "CASHOUT", voitto)
                    print(" ")
                    print("Cashoutataan.")
                    time.sleep(2)
                    print(" ")
                    print("---=====================---")
                    print(f"       Uusi saldo: {saldo}€")
                    print("---=====================---")
                    print(" ")
                    return
                elif jatka == "k":
                    kerros += 1
                    break
                else:
                    print("Virheellinen valinta, kirjoita k tai e")
                    time.sleep(1)
    print(" ")
    print("VOITIT TORNIN")  
    saldo += voitto
    tallenna("TOWER", "TORNI VOITETTU", voitto)
    print("Saldo:", saldo, "€")
    
#def blackjack():
    #print("---=== BLACKJACK ===---")
    #print("saldo:", saldo)
    
def coinflip():
    saldo = tarkistus("Kuinka paljon saldoa sinulla on? ", 1, 999999)
    print("saldo", saldo, "€")
    print(" ")
    panos = tarkistus("Kuinka paljon haluat panostaa? ", 1, 999999)
    panos = tarkistapanos(panos, saldo)
    if panos == saldo:
            print("Vau! All in :D!")
    for i in range(3):
        print("Ladataan peliä" + "." * (i+1))
        time.sleep(1.5)
    
    print(" ")
    print("---=== TERVETULOA COINFLIPPIIN ===---")
    print(" ")
    while True:
        valinta = input("Kumman valitset: (Kruuna vai Klaava)").upper()
        ebg = ["KRUUNA", "KLAAVA"]
        if valinta in ebg:
            break
        print("Virheellinen syöte, kirjoita Kruuna tai Klaava")
    print(" ")
    vastaus = random.choice(ebg)
    if valinta == vastaus:
        print("Vastaus oli", vastaus)
        rulettivoitto()
        saldo += panos
        tallenna("COINFLIP", "VOITTO", panos)
    else:
        print("Vastaus oli", vastaus)
        rulettihavio()
        saldo -= panos
        tallenna("COINFLIP", "HÄVIÖ", -panos)
    if valinta == vastaus:
        print("Voitit", panos, "€")
        print("Saldo: ", saldo, "€")
    else:
        print("Voitit 0€")
        print("Saldo: ", saldo, "€")

main()
