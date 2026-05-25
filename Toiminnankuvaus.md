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
