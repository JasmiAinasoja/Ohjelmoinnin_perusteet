print("Program starting.\n")

while True:
    print("Options:")
    print("1 - Celsius to Fahrenheit")
    print("2 - Fahrenheit to Celsius")
    print("0 - Exit")

    choice = input("Your choice: ")

    if choice == "1":
        celsius = float(input("Insert the amount of Celsius: "))
        fahrenheit = celsius * 1.8 + 32
        print(f"{round(celsius, 1)} °C equals to {round(fahrenheit, 1)} °F\n")

    elif choice == "2":
        fahrenheit = float(input("Insert the amount of Fahrenheit: "))
        celsius = (fahrenheit - 32) / 1.8
        print(f"{round(fahrenheit, 1)} °F equals to {round(celsius, 1)} °C\n")

    elif choice == "0":
        print("Exiting...\n")
        print("Program ending.")
        break

    else:
        print("Unknown option.\n")