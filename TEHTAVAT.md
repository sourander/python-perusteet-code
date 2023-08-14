# Tehtävänannot

Tehtävät on jaettu aihealuettain otsikoiden alle. Tehtävät on pyritty järjestämään vaikeusjärjestykseen, joten voit tehdä ne järjestyksessä alusta loppuun.

# Osio 0: Esitehtävä

## Tehtävä 0.1: harjoitukset.helloworld

Ensimmäinen tehtävä ei varsinaisesti ole tehtävä laisinkaan, vaan sait valmiiksi sen seuraamalla `README.md`-tiedoston ohjeita. Tehtävästä voi kuitenkin ottaa mallia seuraaviin tehtäviin. Kuvitteellinen tehtävänanto olisi:

> Luo moduuli `harjoitukset.helloworld`. Kirjoita moduuliin funktio `hello_world` joka palauttaa merkkijonon `"Hello World!"`. Isoilla ja pienillä kirjaimilla, kuten myös välilyönneillä sekä huutomerkillä, on merkitystä.

Vastaus on tehty jo valmiiksi, joten älä muokkaa sitä. Moduuli on tiedostos `harjoitukset/helloworld.py`, ja se sisällä on seuraavat rivit, jotka toteuttavat ohjelman.:
```python
def hello_world():
    return "Hello World!"
```

## Tehtävä 0.1: mypy

Myös testi `test_mypy` suotiutuu automaattisesti aluksi. Mypy ajaa staattisen tyypityksen testejä Python-koodia vasten. Se auttaa sinua tilanteissa, joissa vika johtuu esimerkiksi siitä, että yrität ynnätä yhteen merkkijonon ja numeron: `"kissa" + 5`. Tällöin testi palautaisi seuraavan virheen:

```log
FAILED tests/test_mypy.py::test_mypy - AssertionError: vastaukset\strings.py:2: error: Unsupported operand types for + ("str" and "int")  [operator]
```

# Osio 1: Merkkijonot

## Tehtävä 1.1: Vokaalit

Luo moduuli `harjoitukset.merkkijonot`. Kirjoita moduuliin funktio `count_vowels`, joka laskee kaikki **suomen kielen vokaalit** merkkijonosta `s`, joka funktioon syötetään. Funktion tulee palauttaa kokonaisluku.