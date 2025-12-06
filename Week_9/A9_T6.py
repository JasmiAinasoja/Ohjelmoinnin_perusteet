########################################################
# Task A9_T6
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################


def show_menu() -> None:
    print("\nOptions:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

def save_lines(lines: list[str]) -> None:
    if not lines:
        print("Nothing to save.")
        return
    filename = input("Insert filename: ")
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
    except Exception as e:
        print("Error while saving: {}".format(e))

def main() -> None:
    print("Program starting.")
    lines: list[str] = []
    first_menu = True

    try:
        while True:
            if not first_menu:
                print()
            first_menu = False

            show_menu()
            choice = input("Your choice: ").strip()

            if choice == "1":
                text = input("Insert text: ")
                lines.append(text)

            elif choice == "2":
                if lines:
                    save_lines(lines)
                else:
                    print("Nothing to save.")

            elif choice == "0":
                break

            else:
                print("Unknown option!")

    except KeyboardInterrupt:
        if lines:
            print("Keyboard interrupt and unsaved progress!")
            ans = input("Save before quit(y/n)?: ").strip().lower()
            if ans in ("y", "yes"):
                save_lines(lines)
        else:
            print("Closing suddenly.")

    print("Program ending.")

if __name__ == "__main__":
    main()
