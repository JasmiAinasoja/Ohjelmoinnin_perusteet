# Tiedostojen hallinta ja virheiden käsittely

import sys

def readLines(PFilepath: str, Plines: list) -> None:
    try:
        Filehandle = open(PFilepath, 'r', encoding="UTF-8")
        Line = Filehandle.readline()
        while Line != '':
            Plines.append(Line)
            Line = Filehandle.readline()
    except FileNotFoundError:
        print("Filu hukassa.")
        # Luodaan tässä uusi filu
    except Exception:
        print("Could not read file.")
        sys.exit(1)
    return None

def main() -> None:
    print("Program starting.")
    Lines: list[str] = []
    Filename = input("Insert filename: ")
    readLines(Filename, Lines)
    print(f"Reading from file: {Filename}")
    for Line in Lines:
        print(Line)
    print("Program ending.")

    return None

main()