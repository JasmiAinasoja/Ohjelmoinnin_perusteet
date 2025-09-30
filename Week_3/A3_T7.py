print("Program starting.")
print("Testing decision structures.")
integer = int(input("Insert an integer: "))

print("Options:")
print("1 - In one multi branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    print("Using one multi-branched decision structure.")
    if integer >= 400:
        result = integer + 44
        print(f"Result is {result}")
    elif integer >= 200:
        result = integer + 22
        print(f"Result is {result}")
    elif integer >= 100:
        result = integer + 11
        print(f"Result is {result}")

elif choice == 2:
    print("Using multiple independent if-statements structure.")
    if integer >= 400:
        result = integer + 44 + 22 + 11
        print(f"Result is {result}")
    elif integer >= 200:
        result = integer + 22 + 11
        print(f"Result is {result}")
    elif integer >= 100:
        result = integer + 11
        print(f"Result is {result}")

elif choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print("\nProgram ending.")