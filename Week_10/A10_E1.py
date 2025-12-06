########################################################
# Task A10_E1
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################

import sys
from A10_ELib import read_values, quick_sort, format_values

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    try:
        values: list[int] = read_values(filename)
    except FileNotFoundError:
        print(f"Error! File '{filename}' not found.")
        print("Program ending.")
        sys.exit(1)
    except PermissionError:
        print(f"Error! No permission to read '{filename}'.")
        print("Program ending.")
        sys.exit(1)
    except ValueError as e:
        print(e)
        print("Program ending.")
        sys.exit(1)
    except OSError as e:
        print(f"Error! Could not read '{filename}': {e}")
        print("Program ending.")
        sys.exit(1)

    print(f"Raw '{filename}' -> {format_values(values)}")

    asc = quick_sort(values, reverse=False)
    print(f"Ascending '{filename}' -> {format_values(asc)}")

    desc = quick_sort(values, reverse=True)
    print(f"Descending '{filename}' -> {format_values(desc)}")

    print("Program ending.")

if __name__ == "__main__":
    main()
