def add(PAddend1: float, PAddend2: float) -> float:
    """Laskee kahden luvun summan."""
    return PAddend1 + PAddend2

def subtract(PMinuend: float, PSubtrahend: float) -> float:
    """Vähentää toisen luvun ensimmäisestä."""
    return PMinuend - PSubtrahend

def multiply(PMultiplicant: float, PMultiplier: float) -> float:
    """Kertoo kaksi lukua keskenään."""
    return PMultiplicant * PMultiplier

def divide(PDividend: float, PDivisor: float) -> float:
    """Jakaa ensimmäisen luvun toisella."""
    if PDivisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return PDividend / PDivisor

def askChoice(valid_choices: list[int]):
    while True:
        try:
            choice = int(input("Your choice: "))
            if choice in valid_choices:
                return choice
            
            print(f"Invalid choice. Please select one of: {valid_choices}")

        except ValueError:
            print("Invalid input. Please enter a number.")

        except (KeyboardInterrupt, EOFError):
            print("User interrupted. Cancelling.")


def showMenu(options: list[str]):
    print("Options:")

    for option in options:
        print(option)


def askInt(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        

        except ValueError:
            print("Please enter a valid integer.")

        except (KeyboardInterrupt, EOFError):
            print("User interrupted. Cancelling.")
            return False
