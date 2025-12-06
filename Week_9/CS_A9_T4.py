# Itse nostettu virhetilanne
# Astemerkki: alt + 0176

TEMP_MIN = -200
TEMP_MAX = 1000

def collectCelsius() -> float:

    Celsius = float(input("Insert Celsius: "))
    if (Celsius < TEMP_MIN) or (Celsius > TEMP_MAX):
        raise Exception(f"{Celsius} out of range")

    return Celsius
def main() -> None:
    print("Program starting.")
    try:
        Celsius = collectCelsius()
        print(f"You inserted {Celsius}°C")
    except Exception as err:
        print(err)
    print("Program ending.")
    return None

main()