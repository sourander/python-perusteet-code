# Tehtävänannot

Tehtävät on jaettu aihealuettain otsikoiden alle. Tehtävät on pyritty järjestämään vaikeusjärjestykseen, joten voit tehdä ne järjestyksessä alusta loppuun.



## Muuttajatyyppien vihjaus

Funktio voi olla tunnukseltaan (eng. signature) esimerkiksi `do_it(a: str) -> int`: sisään menee merkkijono, takaisin palautuu kokonaisluku. Esimerkin funktion nimi on `do_it`, se ottaa sisään yhden argumentin (`a`), ja palauttaa kokonaisluvun). Vihjeiden lisääminen funktioon määritykseen ei ole pakollista, mutta se parantaa luettavuutta.

Käytännössä saman funktion voi toteuttaa kummalla tahansa tavalla alla olevasta tavasta:

```python
# Tapa 1: Ei vihjeitä muuttujatyypeistä
def do_it(a):
    return len(a)

# Tapa 2: Vihje sekä parametrin että palautuksen tyypistä
def do_it(a:str) -> int:
    return len(a)
```

Huomaa, että **tämän kurssin tehtävissä oletetaan**, että lisäät tyyppivihjeet (eng. type hints) aivan jokaiseen funktioon. Tyyppivihjeiden käyttö vaatii Python 3.5 tai uudemman.



# Osio 0: Esitehtävä

## Tehtävä 0.1: tasks.helloworld

Ensimmäinen tehtävä ei varsinaisesti ole tehtävä laisinkaan. Tehtävä on tehty sinun puolesta, jotta voit testata `pytest`-kirjaston toiminnan, kuten `README.md`-tiedostossa neuvottiin. Tehtävästä voi kuitenkin ottaa mallia seuraaviin tehtäviin. Kuvitteellinen tehtävänanto olisi:

> Luo moduuli `harjoitukset.helloworld`. Kirjoita moduuliin funktio `hello_world` joka palauttaa merkkijonon `"Hello World!"`. Isoilla ja pienillä kirjaimilla, kuten myös välilyönneillä sekä huutomerkillä, on merkitystä.

Vastaus on tehty jo valmiiksi, joten älä muokkaa sitä. Moduuli on tiedostossa `harjoitukset/helloworld.py`. Tiedoston sisältö on:
```python
def hello_world() -> str:
    return "Hello World!"
```

## Tehtävä 0.1: mypy

Myös testi `test_mypy` suotiutuu automaattisesti aluksi. Mypy ajaa staattisen tyypityksen testejä Python-koodia vasten. Se auttaa sinua tilanteissa, joissa vika johtuu esimerkiksi siitä, että yrität ynnätä yhteen merkkijonon ja numeron: `"kissa" + 5`. Tällöin testi palautaisi seuraavan virheen:

```log
FAILED tests/test_mypy.py::test_mypy - AssertionError: vastaukset\strings.py:2: error: Unsupported operand types for + ("str" and "int")  [operator]
```





# Osio 1: Merkkijonot

Tämän osion funktioita yhdistää se, että ne kaikki vaativat argumentteina vain ja ainoastaan merkkijonoja. Palautuvan arvon tyyppi riippuu tehtävästä.


## Tehtävä 1.1: tasks.strings:generate_zip_name

Luo moduuli `tasks.strings`. Tee moduulin sisälle funktio `generate_zip_name`, joka ottaa sisään neljä parametriä: applikaation nimen, version, prosessoriarkkitehtuurin sekä tiedostopäätteen. Jos kutsu on `generate_zip_name("myApp", "1.0", "x86_64", "zip")` niin takaisin tulee palautua merkkijono `"myApp-1.0-x86_64.zip"`

## Tehtävä 1.2: tasks.strings:is_a_in_b

Luo aiemman tehtävän kanssa samaan moduuliin, `tasks.strings`, funktio. Funktion nimi on `is_a_in_b` ja sen parametrit ovat kaksi merkkijonoa. Funktio palauttaa Boolen muuttujan (True tai False), joka indikoi, löytyykö merkkijono a merkkijonon b sisältä. Funktion tulee käsitellä pieniä ja suuria kirjaimia keskenään samoina. Esimerkiksi kutsu `is_a_in_b("kissa", "Lemmikkini nimi on Kissa.")` palauttaa True. Myös `is_a_in_b("from taulu", "SELECT * FROM TAULU")` palauttaa True.

## Tehtävä 1.2: tasks.strings:count_vowels

Käytä yhä samaa moduulia `tasks.strings`. Luo funktio `count_vowels`, joka laskee kaikki **suomen kielen vokaalit** merkkijonosta, joka syötetään funktioon parametrina. Funktion tulee palauttaa kokonaisluku.

## Tehtävä 1.3: tasks.strings:is_palindrome

Käytä yhä samaa moduulia `tasks.strings`. Luo moduuli `is_palindrome`. Funktio palauttaa Boolen muuttujan (True | False), joka indikoi, onko sille syötetty parametri suomen kielessä palindromi vai ei. Joitakin sääntöjä:

1. Isot ja pienet kirjaimet tulee nähdä keskenään samoina.
2. Erikoismerkkejä (ei-aakkosia) ei tule ottaa huomioon.
3. Merkkijonossa pitää olla 2 tai enemmän kirjainta.
4. Funktion ei tarvitse ottaa kantaa siihen, ovatko sanat oikeita sanoja.





# Osio X: Tiedostot

> Pohjustus tiedostoihin. Luo kaikki projektin vaativat tiedostot projektin juureen eli `data/`-kansioon. Kansiota ei ole olemassa vaan sinun tulee luoda se ohjelmallisesti kun tehtävä näin vaatii. Älä rautakoodaa polkua tähän hakemistoon, vaan käytä ROOT_DIR-muuttujaa, jonka voit ladata mihin tahansa projektin tiedostoon näin: `from tasks import ROOT_DIR`. Käy katsomassa `tasks/__init__.py`-tiedoston sisältö, jotta näet kuinka kyseinen muuttuja saa arvonsa.