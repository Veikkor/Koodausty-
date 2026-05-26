# Toiminnan kuvaus
"Kasino"-ohjelmani on Pythonilla tehty tekstipohjainen kasinopeli, jossa käyttäjä voi pelata useita eri pelejä komentorivillä.

Ohjelmassa käyttäjä voi valita peleistä
1. Ruletti
2. Tower
3. Coinflip

Pelaaja syöttää aluksi saldon, sekä halutun panoksen. Panoksen pitää olla saldon sisällä sekä se ei voi olla alle 1 tai yli 999999. 
Ohjelma tarkistaa syötteiden toimivuuden eikä hyväksy virheellistä syötettä.

- Ruletti käyttää satunnaisesti arvottua numeroa väliltä 0–36 ja pelaaja voi panostaa väriin, numeroon, parilliseen/parittomaan, riviin tai alueeseen.
- Tower-pelissä pelaaja etenee kerroksittain välttäen pommeja ja voi cashoutata voittonsa milloin tahansa.
- Coinflip-pelissä käyttäjä valitsee kruunan tai klaavan, jonka jälkeen ohjelma arpoo kolikon tuloksen.

Ohjelma tallentaa kaikki pelaajan voitot sekä häviöt ja näyttää missä pelissä ne tapahtuivat ja paljonko tulos oli. Käyttäjä voi tarkistella pelihistoriaansa pelivalikosta

## Tärkeimmät koodinkohdat
Koodissa on tehty monia erilaisia funktioita tekemään koodin rakenteesta fiksumman

- Tarkistus
    - Olen tehnyt funktion joka auttaa tarkistamaan että saldoa ja panosta kysyttäessä, väärän syötteen laittaminen aiheuttaa virheilmoituksen ja kysyy syötettä uudelleen. Funktiota pystyi myös käyttämään hyvin ruletissa joissain panostustavan valintakohdissa
- Tekstitarkistus
    - Se on funktio, jonka avulla voin tarkistaa ruletissa panostustavan ilman joka kohdassa saman säännön toistamista
- Tarkistapanos
    - Funktio tarkistaa kutsuttaessa aina onko annettu panos oikeanlainen, kutsun koodissa funktiota aina panoksen laittamisen jälkeen
- Tallenna
    - Tallenna funktio mahdollistaa joka voiton ja häviön kohdalla niiden tallentamisen uuteen tiedostoon
- Ruletti
    - Funktion sisällä on koko ruletti peli ja sen toiminta
- Tower
    - Funktion sisällä on koko tower peli ja sen toiminta
- Coinflip
    - Funktion sisällä on koko coinflip peli ja sen toiminta
- Main
    - Kaikista tärkein funktio, funktiota kutsuttaessa ohjelma alkaa

## Tiedostotallennus
Ohjelma tallentaa aina peliä pelatessa pelaajan voitot ja häviöt erilliseen tiedostoon talteen. Tiedot tallennetaan muodossa, esimerkki: 

"COINFLIP | VOITTO | 15€" 

Tällä tavalla pelaaja voi seurata voittoja ja häviöitänsä ja laskea vaikka kuinka paljon hän on yhteensä voittanut ja hävinnyt
