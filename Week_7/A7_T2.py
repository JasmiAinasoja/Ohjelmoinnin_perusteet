def askIntegers(Values: list[int]):
    Feed = input("Insert comma separated integers: ")
    for Value in Feed.split(','): # Split input by commas
        if Value.isnumeric():
            Values.append(int(Value)) # Convert to int and add to the end of the list
        else:
            print(f"Invalid value '{Value}' detected.")
            continue
    return None

def analyze(Values: list[int]):
    Sum = 0
    # Check if the list is empty
    if len(Values) == 0:
        print("No values to analyze.")
    else:
        for Value in Values: # Loop through Values list
            Sum += Value
        print(f"There are {len(Values)} integers in the list.")
        Parity = 'even' if Sum % 2 ==0 else 'odd'
        print(f"Sum of the integers is {Sum} and it's {Parity}")
    return None


def main ():
    print("Program starting.")
    Values: list[int] = []
    askIntegers(Values) # Jump to askIntegers function and send a REFERENCE to the list as a function parameter.
    analyze(Values) # Jump to analyze function and send a REFERENCE to the list as a function parameter.

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()