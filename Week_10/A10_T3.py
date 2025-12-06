########################################################
# Task A10_T3
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################

import sys

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    if n <= 1:
        return None

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            a = PValues[j]
            b = PValues[j + 1]
            if PAsc:
                if a > b:
                    PValues[j], PValues[j + 1] = b, a
                    swapped = True
            else:
                if a < b:
                    PValues[j], PValues[j + 1] = b, a
                    swapped = True

        if not swapped:
            break

    return None

def read_values(filename: str) -> list[int]:
    values: list[int] = []
    with open(filename, "r", encoding="utf-8") as f:
        for raw in f:
            s = raw.strip()
            if s == "":
                continue
            try:
                num = int(s)
            except ValueError:
                raise ValueError(f"Error! '{s}' couldn't be converted to int.")
            values.append(num)
    return values

def format_values(values: list[int]) -> str:
    """Join values as 'v1, v2, v3'."""
    return ", ".join(str(v) for v in values)

def main() -> None:
    print("Program starting.")

    if len(sys.argv) == 2:
        filename = sys.argv[1]
        print(f"The filename '{filename}' was passed via CLI.")
    else:
        filename = input("Insert filename: ").strip()

    try:
        values = read_values(filename)
    except FileNotFoundError:
        print(f"Error! File '{filename}' not found.")
        print("Program ending.")
        return
    except PermissionError:
        print(f"Error! No permission to read '{filename}'.")
        print("Program ending.")
        return
    except OSError as e:
        print(f"Error! Could not read '{filename}': {e}")
        print("Program ending.")
        return
    except ValueError as e:
        print(e)
        print("Program ending.")
        return

    print(f"Raw '{filename}' -> {format_values(values)}")

    asc = list(values)
    bubbleSort(asc, PAsc=True)
    print(f"Ascending '{filename}' -> {format_values(asc)}")

    desc = list(values)
    bubbleSort(desc, PAsc=False)
    print(f"Descending '{filename}' -> {format_values(desc)}")

    print("Program ending.")

if __name__ == "__main__":
    main()