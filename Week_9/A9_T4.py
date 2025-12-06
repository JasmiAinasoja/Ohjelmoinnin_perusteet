########################################################
# Task A9_T4
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################



TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius(feed: str) -> float:
    try:
        c = float(feed)
    except ValueError:
        raise ValueError("could not convert string to float: '{}'".format(feed))

    if c < TEMP_MIN or c > TEMP_MAX:
        raise Exception("{} temperature out of range.".format(c))

    return c

def main():
    print("Program starting.")
    raw = input("Insert Celsius: ")

    try:
        celsius = collectCelsius(raw)
        print("You inserted {:.1f} °C".format(celsius))
    except Exception as e:
        print(e)

    print("Program ending.")

if __name__ == "__main__":
    main()
