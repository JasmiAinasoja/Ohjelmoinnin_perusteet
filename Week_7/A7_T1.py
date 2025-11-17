def askPositiveInteger():
    PositiveInt = -1
    Feed = input("Insert positive integer (negative stops): ")
    if Feed.isnumeric():
        PositiveInt = int(Feed)
    return PositiveInt

def displayIntegers(Numbers: list[int]):
    if len(Numbers) == 0:
        print("No integers to display.")
    else:
        print(f"Displaying {len(Numbers)} integers:")
        for i in range(len(Numbers)):
            print(f"- Index {i} => Ordinal {i+1} => Integer {Numbers[i]}")
    return None


def main():
    print("Program starting.")
    print("Collect positive integers.")
    PositiveIntegers: list[int] = []
    CurrentInteger = askPositiveInteger()
    while CurrentInteger >= 0:
        PositiveIntegers.append(CurrentInteger)
        CurrentInteger = askPositiveInteger()
    print("Stopped collecting positive integers.")

    displayIntegers(PositiveIntegers)

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()