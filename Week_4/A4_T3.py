print("Program starting.\n")

value1 = int(input("Insert starting value: "))
value2 = int(input("Insert stopping value: "))

print("\nStarting while-loop:")
current = value1
while current <= value2:
    print(current, end=' ')
    current += 1

print("\n\nProgram ending.")
