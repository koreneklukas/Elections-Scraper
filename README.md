
# 🗳 Elections Scraper – Projekt 3 (Engeto Online Python Akademie)

Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017.  
Odkaz k prohlédnutí výsledků najdete [zde](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

---

## 📌 Popis projektu

Skript `main.py` načte výsledky voleb z veřejného webu volby.cz pro zadaný kraj nebo okres.  
Pro každou obec získá detailní výsledky včetně počtu voličů, obálek, platných hlasů a výsledků všech kandidujících stran.  
Výsledky jsou uloženy do CSV souboru, který si uživatel určí při spuštění.

---

## ⚙️ Instalace knihoven

Knihovny použité v projektu jsou zapsány v souboru `requirements.txt`.

Doporučuji použít virtuální prostředí.  
Pro instalaci spusť:

```bash
pip3 install -r requirements.txt
```

---

## 🚀 Spuštění projektu

Spuštění skriptu `main.py` v příkazové řádce vyžaduje **2 argumenty**:

```bash
python main.py <url-obce-nebo-kraje> <nazev-vystupniho-souboru.csv>
```

Například:

```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100" vysledky_praha.csv
```

Pokud nejsou zadány přesně 2 argumenty, skript vypíše upozornění:

```
 Chyba: Zadej 2 argumenty – URL a název výstupního CSV souboru.
 Příklad: python main.py https://... vysledky.csv
```

---

## 💻 Ukázka projektu

Výsledky hlasování pro Prahu:

- **1. argument (URL):**  
  `https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100`
- **2. argument (výstupní CSV):**  
  `vysledky_praha.csv`

### Spuštění programu:

```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100" vysledky_praha.csv
```

### Průběh stahování v terminálu:

```
 Načítám stránku s výsledky...
 Nalezeno 57 obcí. Zpracovávám...
   ➜ 1/57: Praha 1
   ➜ 2/57: Praha 2
   ...
 Hotovo! Výsledek uložen do vysledky_praha.csv
```

### Částečný výstup CSV:

```csv
Kód obce;Název obce;Voliči v seznamu;Vydané obálky;Platné hlasy;Občanská demokratická strana;...
500001;Praha 1;5678;3456;3400;123;...
500002;Praha 2;6789;4567;4500;234;...
```

---

## 📁 Struktura projektu

```
Elections-Scraper/
│
├── main.py              # hlavní Python skript
├── requirements.txt     # seznam požadovaných knihoven
└── README.md            # tento soubor s dokumentací
```

---

## 📄 Obsah `requirements.txt`

```text
requests
beautifulsoup4
```

---

## ✍️ Autor

Třetí projekt v rámci **Engeto Online Python Akademie**  
**Autor:** Lukáš Kořenek  
📧 **E-mail:** koreneklukas@seznam.cz
