print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
Name = input("Before the menu, please insert your name: \n")
print("Options:")
print("1 - Print welcome message")
print("0 - Exit")

Num = int(input("Your choice: "))

if Num == 1:
    print(f"Welcome {Name}!")
elif Num == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")

