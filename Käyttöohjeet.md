# Käyttöohjeet
## Käynnistys
1. Avaa komentokehote
2. Siirry projektikansioon
3. Käynnistä ohjelma komennolla:

"python Kasino.py"

# Päävalikko
Kun käynnistät ohjelman, näet päävalikon.
Valikossa voit valita mitä peliä haluat pelata, vaihtoehdot ovat:

1. Ruletti
2. Tower
3. Coinflip
4. Pelihistoria

Voit valita mitä peliä haluat pelata kirjoittamalla halutun pelin numeron (1 - 3).
Pelin valittaessa sinulle tulostuu pelin ohjeet sekä säännöt. Tai voit valita pelihistoria (4), joka tulostaa pelihistorian,
eli pelin, voitto vai häviö ja summan joka voitettiin tai hävittiin

# Saldo ja panostaminen
- Jokaisen pelin alussa kysytään pelaajan saldo
- Sen jälkeen asetetaan panos
- Saldo ja panos täytyy olla 1 - 999999
- Panos ei myöskään voi olla suurempi kuin saldo

# Eri pelien toiminta

## Ruletti
Ruletissa voit panostaa
- Väriin
- Parilliseen / parittomaan
- Alueeseen
- Numeroon
- Riviin

Voitot määräytyvät valinnan perusteella
- 🟥 Väri               x2
- 🔢 Parillinen/Pariton x2
- 📍 Alue               x2
- 🎯 Numero             x35
- 📚 Rivi               x3

## Tower
Towerissa on torni, jossa on 5 kerrosta. Jokaisella kerroksella on 5 laattaa. Yhdessä laatassa kolmesta on pommi, joka aiheuttaa häviön. 
Jos kuitenkin arvaat turvallisen laatan, voit jatkaa seuraavalle kerrokselle ja voittosi kasvaa
- Valitse laatta 1-3
- Jos hävisit, peli kertoo uuden saldosi
- Jos voitit, peli kysyy haluatko jatkaa vai cashoutata, jatkaessa siirryt seuraavalle kerrokselle, cashoutatessa peli tulostaa uuden saldosi
- Voit cashoutata millon tahansa

## Coinflip
Coinflip on peli, jossa kone "heittää" kolikkoa ja sinun pitää arvata kummalle puolelle se laskeutuu
- Valitse Kruuna tai Klaava
- Kolikko heitetään aina satunnaisesti
- Oikea arvaus = 2x panoksesi

## Pelihistoria
Pelihistoriassa voi nähdä pelatut pelit ja voititko/hävisitkö ja kuinka paljon voitit(hävisit


## Virheelliset syötteet
Jos käyttäjä syöttää
- Väärän tekstin
- Liian ison tai pienen numeron
- Väärän arvon
Ohjelma ilmoittaa aina siitä ja kysyy käyttäjältä syöttämään syötteen uudelleen

## Sulkeminen
Voit sulkea ohjelman
- painamalla "ctrl + c"
- Sulkemalla terminaalin
