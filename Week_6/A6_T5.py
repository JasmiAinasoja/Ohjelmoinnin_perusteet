SEPARATOR = ";"

def readValues(filename) -> list:
    values = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                values.append(int(line))
    return values


def analyseNumbers(values) -> str:
    if not values:
        return f"0{SEPARATOR}0{SEPARATOR}0{SEPARATOR}0.00"
    count = len(values)
    total = sum(values)
    greatest = max(values)
    average = total / count
    return f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}"

def displayResults(filename, analysis):
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print(f"Count{SEPARATOR}Sum{SEPARATOR}Greatest{SEPARATOR}Average")
    print(analysis)
    print("\n#### Number analysis - END ####")

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    analysis = analyseNumbers(values)
    displayResults(filename, analysis)
    print("Program ending.")

if __name__ == "__main__":
    main()