# Python Perusteet

# JavaScript perusteet

Tämä kurssi on koodattu Python 3:lla. Pythonon dokumentaatio löytyy [täältä](https://docs.python.org/3/).

* Tehtävät tehdään seuraamalla [tehtävänantoja](docs/TEHTAVAT.md).
  * Kaikki tehtävät toteutetaan `tasks/`-hakemistoon.
* Tehtävät testataan ajamalla testit. Lue ohje alta.

Tehtävät kannattaa tehdä tuoreimmalla vakaalla Python 3:lla, joka on tämän kirjoitushetkellä Python 3.11.

**HUOM:** Tämän ohjeen hakemistopolut ovat relatiivisia tämän projektin juureen nähden (eli siihen kansioon, jossa juuri tämä `README.md`-tiedosto sijaitsee.) Hakemistopolut on kirjoitettu POSIX-polkuja käyttäen, joten tiedostopolun hakemistojen välisenä erottimena käytetään kauttaviivaa (eng. slash, `/`). Mikäli käytät Windowsia, korvaa ne kenoviivalla (eng. backslash, `\`).

# Ennen kuin aloitat

Tämän kurssin tehtävät voi tarkistaa itse. Tehtävät tarkistetaan Pythonin `pytest`-kirjastolla. Varmista ensin, että `pytest` toimii oletetulla tavalla. Kurssin ensimmäinen tehtävä, Hello World, on tehty jo valmiiksi. Testaa se alla olevalla koodilla.

## Testaa Hello World

```sh
# Asenna riippuvuudet
$ pip install requirements.txt

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

Yllä ajettu testi ajoi testifunktion (eng. test function nimeltään `test_hello_world`) yhden testitiedoston (eng. test file nimeltään `tests/test_helloworld.py`) sisällä. Mikäli yllä oleva komento palautti onnistuneen testiajon, ympäristösi toimii ja olet valmis aloittamaan tehtävät. Mikäli saat virheilmoituksen `'pytest' is not recognized as an internal or external command, operable program or batch file.` tai `pytest: command not found`, et ole joko asentanut pytestiä ohjeiden mukaisesti, tai sinulla ei ole virtuaaliympäristö aktivoituna.

## Tehtävän tekeminen

1. Tehtävät on tarkoituksella aloittajalle haastavia; lue Pythonin dokumentaatiota kun teet tehtäviä, kysy neuvoa muilta, yritä ja erehdy. 
2. Tehtävät voi tehdä millä tahansa tekstieditorilla, mutta Visual Studio Codea on suositeltu ja tunneilla neuvottu.
3. Aja kaikki tehtävät projektin juuresta eli siis kansiosta `.../python-perusteet-code/`. Komentoriviesimerkki koodin ajamiseen on: `python tasks/helloworld.py`

> Vinkki: mikäli haluat ajaa koodin siten, että siitä jää interaktiivinen sessio käyntiin koodin suorittamisen jälkeen, lisää parametri -i, eli `python -i <polku-tiedostoon>`. Interaktiivinen sessio sulkeutuu komennolla `quit()`.

**VSCODE-VINKKI!** Visual Studio Coden koodieditorin oikean yläkulman `Run Python File` ajaa koodin oletusasetuksilla siitä kansiosta käsin, missä kyseinen tiedosto sijaitsee. Tämä toimii niin kauan kunnes haluat tuoda (eng. import) kirjaston sisään relatiivista moduulipolkua käyttäen, kuten `import tasks.something`. Mikäli skripti on vaikkapa kansiossa `tasks/`, koodi kaatuu `import`-komentoon, sillä moduulia `tasks/tasks/something/` ei ole olemassa. Mikäli haluat käyttää tätä, sinun pitää huolehtia, että VS Code asettaa koodin ajamisen ajaksi ympäristömuuttujan PYTHONPATH arvoksi projektikansion. Yksi tapa tehdä tämä on luoda `Run and Debug`-paneelin avulla (ruudun vasemmalla) uusi konfiguraatio, ja lisätä konfiguraatio-JSON:iin rivi `"env":{"PYTHONPATH": "${workspaceFolder}"}`.


## Testaa kaikki tehdyt

1. Lue seuraavan tehtävänanto huolella
2. Toteuta koodi `tasks`-hakemiston alle määrättyyn tiedostoon.
3. Aja testit: `pytest`.
4. Muokkaa koodia kunnes kyseinen tehtävä on **PASSED** (vastakohta on **FAILED**, aloittamaton on **SKIPPED**).
5. Tallenna ja lisää versionhallintaan.
6. Siirry seuraavaan tehtävään.

Testi (Kohta 3) ajetaan lyhyesti ja ytimekkäästi komennolla:
```
pytest
```

Huomaathan, että ne tehtävät, joita et ole aloittanut, sivuutetaan kokonaan: niissä lukee vain **SKIPPED**. Tämä johtuu siitä, että testin etsimää tiedostoa ei löydy. Tämä tapahtuu myös siinä tilanteessa, jos olet nimennyt tiedoston, funktion tai jotakin muuta väärin.

Mikäli haluat hieman tiiviimmän tulosteen, kokeile ajaa skripti quiet-parametrilla eli `pytest -q`. Tyypillisesti tämä on default, mutta `pytest.ini` tiedostossa on asetettu `addopts = -v`. Verbosen ja quietin paremmuus riippuu hieman tilanteesta ja mahdollisesta ongelmasta. Ajoittain ongelman mahdollinen virheilmoitus on helpompi lukea verbose-tilassa.

# Tehtävän palauttaminen

Kun kaikki testit menevät läpi (eli `pytest` palauttaa kaikista tehtävistä **PASSED**), on aika palauttaa tehtävä. Luo `pytest`:stä raportti. Tarvitset sitä varten pluginin `pytest-html`. 

1. Asenna ja aja pytest alla olevalla `--html` parametrillä.
2. Lisää tiedosto versionhallintaan.
3. Palauta tehtävä muualla neuvotulla tavalla (tod.näk. Moodle).

```sh
# Asenna pytest plugin
pip install pytest-html

# bash/linux
pytest --html=report/yyyy-mm-dd-etunimi-sukunimi.html
```