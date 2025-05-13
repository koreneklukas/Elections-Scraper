"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Lukáš Kořenek
email: koreneklukas@seznam.cz
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv

def load_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")

def get_obce_urls(soup):
    urls = []
    rows = soup.select("table tr")[2:]  # přeskočí hlavičku
    for row in rows:
        link = row.select_one("td a")
        if link:
            href = link["href"]
            full_url = "https://www.volby.cz/pls/ps2017nss/" + href
            code = row.select_one("td:nth-child(1)").text.strip()
            name = row.select_one("td:nth-child(2)").text.strip()
            urls.append((code, name, full_url))
    return urls

def parse_detail(code, name, url, party_names_ref):
    soup = load_soup(url)
    summary_table = soup.select("table")[0]
    tds = summary_table.select("td")
    registered = tds[3].text.replace("\xa0", "")
    envelopes = tds[4].text.replace("\xa0", "")
    valid_votes = tds[7].text.replace("\xa0", "")

    # Hlasy pro strany
    parties = {}
    party_tables = soup.find_all("table", {"class": "table"})[1:]
    for table in party_tables:
        rows = table.find_all("tr")[2:]
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                party_name = cols[1].get_text(strip=True)
                votes = cols[2].get_text(strip=True).replace("\xa0", "")
                parties[party_name] = votes

    # Uložíme seznam stran, pokud je to první obec
    if not party_names_ref:
        party_names_ref.extend(parties.keys())

    # Sestavení hlasů podle pořadí stran
    votes_all = [parties.get(party, "0") for party in party_names_ref]
    return [code, name, registered, envelopes, valid_votes] + votes_all

def save_csv(data_rows, party_names, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        header = ["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"] + party_names
        writer.writerow(header)
        writer.writerows(data_rows)

def main():
    if len(sys.argv) != 3:
        print(" Chyba: Zadej 2 argumenty – URL a název výstupního CSV souboru.")
        print(" Příklad: python projekt_3.py https://... vysledky.csv")
        return

    url = sys.argv[1]
    output_filename = sys.argv[2]

    print(" Načítám stránku s výsledky...")
    soup = load_soup(url)
    obce = get_obce_urls(soup)

    print(f" Nalezeno {len(obce)} obcí. Zpracovávám...")

    data_rows = []
    party_names = []

    for index, (code, name, url_detail) in enumerate(obce, start=1):
        print(f"   ➜ {index}/{len(obce)}: {name}")
        row_data = parse_detail(code, name, url_detail, party_names)
        data_rows.append(row_data)

    save_csv(data_rows, party_names, output_filename)
    print(f" Hotovo! Výsledek uložen do {output_filename}")

if __name__ == "__main__":
    main()
