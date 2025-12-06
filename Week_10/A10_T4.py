########################################################
# Task A10_T4
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################

import sys

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    PMerge.clear()
    i, j = 0, 0
    len_l, len_r = len(PLeft), len(PRight)

    if PAsc:
        def goes_left(a, b): return a <= b
    else:
        def goes_left(a, b): return a >= b
    while i < len_l and j < len_r:
        if goes_left(PLeft[i], PRight[j]):
            PMerge.append(PLeft[i])
            i += 1
        else:
            PMerge.append(PRight[j])
            j += 1
    while i < len_l:
        PMerge.append(PLeft[i])
        i += 1
    while j < len_r:
        PMerge.append(PRight[j])
        j += 1

    return None

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    if n <= 1:
        return None

    mid = n // 2
    left = PValues[:mid]
    right = PValues[mid:]

    mergeSort(left, PAsc=PAsc)
    mergeSort(right, PAsc=PAsc)

    merged: list[int] = []
    merge(left, right, merged, PAsc=PAsc)

    PValues[:] = merged
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
    mergeSort(asc, PAsc=True)
    print(f"Ascending '{filename}' -> {format_values(asc)}")

    desc = list(values)
    mergeSort(desc, PAsc=False)
    print(f"Descending '{filename}' -> {format_values(desc)}")

    print("Program ending.")

if __name__ == "__main__":
    main()