# Elections-Scraper
# 🗳 Elections Scraper – Projekt 3 (Engeto Online Python Akademie)

Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017.  
Odkaz k prohlédnutí výsledků najdete [zde](https://www.volby.cz/).

---

## 📌 Popis projektu

Skript `main.py` načte výsledky voleb z veřejného webu volby.cz pro zadaný kraj nebo okres.  
Pro každou obec získá detailní výsledky včetně počtu voličů, obálek, platných hlasů a výsledků všech kandidujících stran.  
Výsledky jsou uloženy do CSV souboru, který si uživatel určí při spuštění.

---

## ⚙️ Instalace knihoven

Knihovny použité v projektu jsou zapsány v souboru `requirements.txt`.

Doporučujeme použít virtuální prostředí.  
Pro instalaci spusť:

```bash
$ pip3 --version                     # ověření verze správce balíčků
$ pip3 install -r requirements.txt  # instalace potřebných knihoven


Spuštění skriptu main.py v příkazové řádce vyžaduje 2 argumenty:
python main.py <url-obce-nebo-kraje> <nazev-vystupniho-souboru.csv>

Například:
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100" vysledky_praha.cs
Pokud nejsou zadány správně oba argumenty, skript upozorní a ukončí se.

Ukázka projektu
Výsledky hlasování pro okres Prostějov:

1. argument (URL):
https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103

2. argument (výstupní CSV):
vysledky_prostejov.csv

Spuštění programu:
python main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv

Průběh stahování:
STAHL JSEM DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
UKLÁDÁM DO SOUBORU: vysledky_prostejov.csv
UKONČUJI election-scraper

Částečný výstup:
code;location;registered;envelopes;valid;Občanská demokratická strana;...
506761;Alojzov;205;145;144;29;...
589268;Bedihošť;834;527;524;51;...
...


Struktura projektu
Elections-Scraper/
│
├── main.py             # hlavní Python skript
├── requirements.txt    # seznam požadovaných knihoven
└── README.md           # tento soubor s dokumentací


 Obsah requirements.txt
requests
beautifulsoup4
