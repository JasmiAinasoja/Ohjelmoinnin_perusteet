########################################################
# Task A10_T6
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################

import copy
import time
from typing import Callable

def show_menu() -> None:
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")

def readValues(filename: str, PValues: list[int]) -> None:
    PValues.clear()
    with open(filename, "r", encoding="utf-8") as f:
        for raw in f:
            s = raw.strip()
            if s == "":
                continue
            try:
                num = int(s)
            except ValueError as e:
                raise ValueError(f"Error! '{s}' couldn't be converted to int.") from e
            PValues.append(num)

def bubbleSort(PNums: list[int]) -> list[int]:
    """
    Stable bubble sort (ascending). Returns a new list.
    """
    arr = list(PNums)
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def quickSort(PNums: list[int]) -> list[int]:
    """
    Functional quick sort (ascending). Returns a new list.
    """
    if len(PNums) <= 1:
        return list(PNums)
    pivot = PNums[len(PNums) // 2]
    left = [x for x in PNums if x < pivot]
    mid  = [x for x in PNums if x == pivot]
    right= [x for x in PNums if x > pivot]
    return quickSort(left) + mid + quickSort(right)

def measureSortingTime(PSortingAlgorithm: Callable[[list[int]], list[int]], PArr: list[int]) -> int:
    """
    Measure elapsed time in nanoseconds for PSortingAlgorithm(PArr).
    Returns the elapsed time. (Sorting result is ignored here.)
    """
    start_ns = time.perf_counter_ns()
    _ = PSortingAlgorithm(PArr)
    end_ns = time.perf_counter_ns()
    return end_ns - start_ns

def main() -> None:
    Values: list[int] = []
    ResultsBlock: str | None = None
    DatasetName: str | None = None

    print("Program starting.")
    while True:
        print()
        show_menu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            fname = input("Insert dataset filename: ").strip()
            try:
                readValues(fname, Values)
                DatasetName = fname
                ResultsBlock = None
            except FileNotFoundError:
                print(f"Error! File '{fname}' not found.")
            except PermissionError:
                print(f"Error! No permission to read '{fname}'.")
            except ValueError as e:
                print(e)
            except OSError as e:
                print(f"Error! Could not read '{fname}': {e}")

        elif choice == "2":
            if not Values or DatasetName is None:
                print("No dataset loaded. Please read dataset values first.")
                continue

            builtin_ns = measureSortingTime(sorted, copy.deepcopy(Values))
            bubble_ns  = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            quick_ns   = measureSortingTime(quickSort, copy.deepcopy(Values))

            lines = []
            lines.append(f"Measured speeds for dataset '{DatasetName}':")
            lines.append(f" - Built-in sorted {builtin_ns} ns")
            lines.append(f" - Buble sort {bubble_ns} ns")
            lines.append(f" - Quick sort {quick_ns} ns")
            ResultsBlock = "\n".join(lines)

            print(ResultsBlock)

        elif choice == "3":
            if not ResultsBlock:
                print("No measured results to save. Measure speeds first.")
                continue
            out_name = input("Insert results filename: ").strip()
            try:
                with open(out_name, "w", encoding="utf-8") as f:
                    f.write(ResultsBlock + "\n")
            except OSError as e:
                print(f"Error! Could not save results to '{out_name}': {e}")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Unknown option!")

    Values.clear()
    print()
    print("Program ending.")

if __name__ == "__main__":
    main()
