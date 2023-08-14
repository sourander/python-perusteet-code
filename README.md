# Python Perusteet

Katso tehtävänannot täältä: **TODO**

# Tehtävien testaaminen

Tämän kurssin tehtävät voi sekä tehdä että tarkistaa itse. Tehtävät tarkistetaan Pythonin `pytest`-kirjastolla.

## Testaa yksi

```sh
# Aja tämä komento
$ pytest tests/test_helloworld.py::test_hello_world --verbose

# Output pitäisi olla tämä
>> configfile: pytest.ini
>> collected 1 item
>> 
>> tests\test_helloworld.py PASSED                      [100%] 
>> 
>> ==================== 1 passed in 0.01s ====================
```

Testi ajoi testifunktion (eng. test function) yhden testitiedoston (eng. test file) sisällä. Mikäli yllä oleva komento palautti onnistuneen testiajon, ympäristösi toimii ja olet valmis aloittamaan tehtävät.

## Tehtävien teko ja testaus

1. Lue yhden tehtävän tehtävänanto huolella
2. Toteuta koodi `tasks`-hakemiston alle. Tarkista tiedostonimet kahdesti.
3. Aja testi.
4. Muokkaa koodia kunnes kyseinen tehtävä on **PASSED** (vastakohta on **FAILED**, aloittamaton on **SKIPPED**).
5. Tallenna ja lisää versionhallintaan.
6. Siirry seuraavaan tehtävään.

Testi ajetaan lyhyesti ja ytimekkäästi komennolla:
```
pytest
```

Huomaathan, että ne tehtävät, joita et ole aloittanut, sivuutetaan kokonaan: niissä lukee vain **SKIPPED**. Tämä johtuu siitä, että testin etsimää tiedostoa ei löydy. Tämä tapahtuu myös siinä tilanteessa, jos olet nimennyt tiedoston, funktion tai jotakin muuta väärin.

Mikäli haluat hieman tiiviimmän tulosteen, kokeile ajaa skripti quiet-parametrilla eli `pytest -q`. Tyypillisesti tämä on default, mutta `pytest.ini` tiedostossa on asetettu `addopts = -v`. Verbosen ja quietin paremmuus riippuu hieman tilanteesta ja mahdollisesta ongelmasta. Ajoittain ongelman mahdollinen virheilmoitus on helpompi lukea verbose-tilassa.

# Tehtävän palauttaminen

Kun kaikki testit menevät läpi, on aika palauttaa tehtävä. Luo `pytest`:stä raportti. Tarvitset sitä varten pluginin `pytest-html`. 

1. Asenna ja aja pytest alla olevalla `--html` parametrillä.
2. Lisää tiedosto versionhallintaan.
3. Palauta tehtävä muualla neuvotulla tavalla (tod.näk. Moodle).

```sh
# Asenna pytest plugin
pip install pytest-html

# bash/linux
pytest --html=report/yyyy-mm-dd-etunimi-sukunimi.html
```