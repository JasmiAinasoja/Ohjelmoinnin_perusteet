########################################################
# Task A9_T1
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################


def main():
    print("Program starting.\n")
    total = 0.0

    while True:
        raw = input("Insert a floating-point value (0 to stop): ")

        if raw.strip() == "0":
            break

        try:
            value = float(raw)
            total += value
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(raw))

    print("\nFinal sum is {:.2f}".format(total))
    print("Program ending.")

if __name__ == "__main__":
    main()
