WEEKDAYS: tuple[str] = (        # Tuple viikonpäivistä, joita CSV-tiedostossa käytetään
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",        # Huom: opettajan CSV-tiedostoissa kirjoitusasu "Saturnday"
    "Sunday"
)

def readFile(filename: str, rows: list[str]):       # Lukee CSV-tiedoston rivit listaan
    print(f'Reading file "{filename}".')
    rows.clear()        # Tyhjennetään lista ennen uuden tiedon lukemista

    with open(filename, "r", encoding="UTF-8") as f:        # Avataan tiedosto UTF-8 enkoodauksella
        next(f)     # Hypätään otsikkorivi yli

        for line in f:      # Käydään läpi jokainen rivi tiedostossa
            if line.strip():        # Tarkistetaan että rivi ei ole tyhjä
                rows.append(line.strip())       # Lisätään rivi listaan ilman ylimääräisiä välilyöntejä


def analyseTimestamps(rows: list[str], results: list[str]):     # Analysoi aikaleimoja ja laskee viikonpäivien esiintymät
    print("Analysing timestamps.")
    results.clear()     # Tyhjennetään tulosten lista ennen uutta analyysiä
    weekday_counts: list[int] = [0] * len(WEEKDAYS)        # Luodaan lista laskureille, yksi per viikonpäivä

    for row in rows:        # Käydään läpi jokainen tiedostosta luettu rivi
        for i,day in enumerate(WEEKDAYS):       # Tarkistetaan jokainen viikonpäivä
            if row.startswith(day):     # Jos rivi alkaa kyseisellä viikonpäivällä
                weekday_counts[i] += 1      # Kasvatetaan kyseisen päivän laskuria

    results.append("### Timestamp analysis ###")       # Lisätään otsikko tuloksiin

    for i, day in enumerate(WEEKDAYS):      # Käydään läpi kaikki viikonpäivät
        results.append(f" - {day} {weekday_counts[i]} stamps")     # Lisätään päivä ja sen esiintymismäärä

    results.append("### Timestamps analysis ###")      # Lisätään päättävä otsikko

def displayResults(results: list[str]):     # Tulostaa analyysitulokset konsoliin
    print("Displaying results.")

    for line in results:        # Käydään läpi jokainen tulosrivi
        print(line)     # Tulostetaan rivi

def main():     # Pääohjelma: koordinoi tiedoston lukemisen, analyysin ja tulosten näytön
    print("Program starting.")

    rows: list[str] = []        # Lista tiedoston riveille
    results: list[str] = []     # Lista analyysin tuloksille

    filename = input("Insert filename: ")       # Pyydetään käyttäjältä tiedostonimi

    readFile(filename, rows)        # Luetaan tiedosto rows-listaan

    analyseTimestamps(rows, results)        # Analysoidaan aikaleimoja ja tallennetaan tulokset

    displayResults(results)     # Näytetään tulokset

    print("Program ending.")

if __name__ == "__main__":
    main()      # Käynnistetään ohjelma