Kasino
import random
def main():
    print("---=== KASINO ===---")
    print("Tervetuloa kasinolle!")
    print("Pelivalikko")
    print("1. Ruletti")
    print("2. Tower")
    print("3. Blackjack")
    pelivalinta = input("Valitse peli: ")
    if pelivalinta == "1":
        ruletti()
            panos = input("Kuinka paljon haluat panostaa?")
    elif pelivalinta == "2":
        tower()
            panos = input("Kuinka paljon haluat panostaa?")
    elif pelivalinta == "3":
        blackjack()
            panos = input("Kuinka paljon haluat panostaa?")
    else:
        print("Virheellinen valinta!")


def ruletti():
    print("---=== RULETTI ===---")
    print("saldo", saldo)
    try:
        panos = int(input("Anna panos: "))
    except ValueError:
        print("Virheellinen panos!")    
        if panos > saldo:
            print("Sinulla ei ole tarpeeksi saldoa!")
            return
        elif panos == saldo:
            print("Vau! All in :D!")
            return
        elif panos <= 0:
            print("Panos ei voi olla nolla tai negatiivinen!")
            return
    
    print("Miten haluat panostaa?")
    tapa = input("Väri, Parillinen/Pariton, 0-18 - 19-36, numero: ")
    if tapa not in ["Väri", "Parillinen/Pariton", "0-18 - 19-36", "numero"]:
        print("Virheellinen panostustapa!")
        return
    elif tapa == "Väri":
        vari = input("Valitse väri (punainen/musta): ")
        if vari not in ["punainen", "musta"]:
            print("Virheellinen väri!")
            return
    elif tapa == "Parillinen/Pariton":
        parillinen_pariton = input("Valitse parillinen vai pariton: ")
        if parillinen_pariton not in ["parillinen", "pariton"]:
            print("Virheellinen valinta!")
            return
    elif tapa == "0-18 - 19-36":
        alue = input("Valitse alue (0-18 vai 19-36): ")
        if alue not in ["0-18", "19-36"]:
            print("Virheellinen alue!")
            return
    elif tapa == "numero":
        try:
            numero = int(input("Valitse numero (0-36): "))
        except ValueError:
            print("Virheellinen numero!")
            return
        if numero < 0 or numero > 36:
            print("Numeron pitää olla 0 ja 36 väliltä!")
        return
    
    def rulettipyora():
        punanen = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        musta = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        parillinen = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        pariton = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        alue1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        alue2 = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        tulos = random.randint(0, 36)
        print("Rulettipyörä pyörii...")
        print("Tulos:", tulos)
        if tapa == "Väri":
            if (vari == "punainen" and tulos in punanen) or (vari == "musta" and tulos in musta):
                print("Voitit!")
                saldo += panos
            else:
                print("Hävisit!")
                saldo -= panos
        elif tapa == "Parillinen()"
def tower():
    print("---=== TOWER ===---")
    print("saldo", saldo)


def blackjack():
    print("---=== BLACKJACK ===---")
    print("saldo", saldo)