########################################################
# Task A10_T5
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################


import sys

def recursiveFactorial(PNum: int) -> int:
    if PNum < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if PNum == 0 or PNum == 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    print("Program starting.")
    raw = input("Insert factorial: ").strip()

    try:
        n = int(raw)
    except ValueError:
        print(f'"{raw}" is not an integer.')
        print("Program ending.")
        return
    if n < 0:
        print("Factorial is not defined for negative integers.")
        print("Program ending.")
        return

    try:
        result = recursiveFactorial(n)
    except RecursionError:
        print("Recursion depth exceeded. Try a smaller number.")
        print("Program ending.")
        return

    print(f"Factorial {n}!")
    print(f"{n} = {result}")
    print("Program ending.")

if __name__ == "__main__":
    main()
