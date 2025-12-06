########################################################
# Task A10_T1
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################

def read_nonempty_lines(filename: str) -> list[str]:
    lines: list[str] = []
    with open(filename, "r", encoding="utf-8") as f:
        for raw in f:
            s = raw.strip()
            if s != "":
                lines.append(s)
    return lines

def show_vertically(values: list[str]) -> None:
    print("# --- Vertically --- #")
    for v in values:
        print(v)
    print("# --- Vertically --- #")

def show_horizontally(values: list[str]) -> None:
    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    try:
        values = read_nonempty_lines(filename)
    except FileNotFoundError:
        print(f'Error! File "{filename}" not found.')
        print("Program ending.")
        return
    except PermissionError:
        print(f'Error! No permission to read "{filename}".')
        print("Program ending.")
        return
    except OSError as e:
        print(f'Error! Could not read "{filename}": {e}')
        print("Program ending.")
        return

    show_vertically(values)
    show_horizontally(values)

    print("Program ending.")

if __name__ == "__main__":
    main()
