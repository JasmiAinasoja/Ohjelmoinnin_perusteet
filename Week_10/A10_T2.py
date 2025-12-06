########################################################
# Task A10_T2
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################

import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    with open(PFilename, "r", encoding="utf-8") as f:
        for raw in f:
            s = raw.strip()
            if s == "":
                continue
            try:
                value = int(s)
            except ValueError:
                raise ValueError(f"Error! '{s}' couldn't be converted to int.")
            PValues.append(value)
    return None

def sumOfValues(PValues: list[int]) -> int:
    Sum = 0
    for v in PValues:
        Sum += v
    return Sum

def productOfValues(PValues: list[int]) -> int:
    Product = 1
    for v in PValues:
        Product *= v
    return Product

def main() -> None:
    Values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    try:
        readValues(filename, Values)
    except FileNotFoundError:
        print(f'Error! File "{filename}" not found.')
        sys.exit(1)
    except PermissionError:
        print(f'Error! No permission to read "{filename}".')
        sys.exit(1)
    except OSError as e:
        print(f'Error! Could not read "{filename}": {e}')
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)

    s = sumOfValues(Values)

    p = productOfValues(Values)

    print("# --- Sum of numbers --- #")
    print(s)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(p)
    print("# --- Product of numbers --- #")

    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
