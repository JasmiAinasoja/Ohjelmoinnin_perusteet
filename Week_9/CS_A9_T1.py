# virheenkäsittelyrakenne
# try -ohjelma yrittää toteuttaa toimenpiteen
# except -tarttuu poikkeukseen
# finally -vapaaehtoinen, tekee virheenkäsittelyn jälkeiset toimet

def main() -> None:
    Sum = 0 # Alusta summamuuttuja
    Value = -1
    print("Program starting.")
    while Value != 0:
        Feed = input("Insert a number, 0 to stop: ")
        try:
            Value = float(Feed)
            Sum += Value # Voisiko tämäkin aiheuttaa virhetilanteen?
        except ValueError: # Tarttuu tyyppierroriin
            print("Selkeä tyyppivirhe")
        except Exception: # Tarttuu mihin tahansa virheeseen, jos meitä ei kiinnosta mikä virheen aiheuttaa
            print(f"\"{Feed}\" is not a number.")
        finally:
            print("Task completed.")
    print("The sum of given numbers is: {Sum}")
    print("Program ending.")
    return None

main()