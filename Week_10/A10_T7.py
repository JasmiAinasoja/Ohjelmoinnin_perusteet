########################################################
# Task A10_T7
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################

import random

random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int) -> None:
    if not PMineField or not isinstance(PMineField, list) or not isinstance(PMineField[0], list):
        raise ValueError("PMineField must be a non-empty 2D list.")
    rows = len(PMineField)
    cols = len(PMineField[0])
    if rows <= 0 or cols <= 0:
        raise ValueError("PMineField must have positive dimensions.")
    if PMines < 0 or PMines > rows * cols:
        raise ValueError("PMines must be in range [0, rows*cols].")

    placed = 0
    while placed < PMines:
        r = random.randrange(rows)
        c = random.randrange(cols)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed += 1
    return None

def calculateNearbys(PMineField: list[list[int]]) -> None:
    if not PMineField or not isinstance(PMineField, list) or not isinstance(PMineField[0], list):
        raise ValueError("PMineField must be a non-empty 2D list.")
    rows = len(PMineField)
    cols = len(PMineField[0])
    if rows <= 0 or cols <= 0:
        raise ValueError("PMineField must have positive dimensions.")

    def in_bounds(rr: int, cc: int) -> bool:
        return 0 <= rr < rows and 0 <= cc < cols

    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            for dr, dc in neighbors:
                rr, cc = r + dr, c + dc
                if in_bounds(rr, cc) and PMineField[rr][cc] == 9:
                    count += 1
            PMineField[r][c] = count
    return None

def generateMinefield(
    PMineField: list[list[int]],
    PRows: int,
    PCols: int,
    PMines: int
) -> None:

    if not isinstance(PRows, int) or not isinstance(PCols, int) or not isinstance(PMines, int):
        raise ValueError("PRows, PCols, and PMines must be integers.")
    if PRows <= 0 or PCols <= 0:
        raise ValueError("PRows and PCols must be positive.")
    if PMines < 0 or PMines > PRows * PCols:
        raise ValueError("PMines must be in range [0, PRows*PCols].")

    PMineField.clear()

    for i in range(PRows):
        PMineField.append([])
        for _ in range(PCols):
            PMineField[i].append(0)

    layMines(PMineField, PMines)

    calculateNearbys(PMineField)
    return None


def print_menu() -> None:
    print("Options:")
    print("1 - Generate minesweeper board")
    print("2 - Show generated board")
    print("3 - Save generated board")
    print("0 - Exit")

def show_board(board: list[list[int]]) -> None:
    if not board:
        print("No board generated yet.")
        return
    for row in board:
        print(row)

def save_board(board: list[list[int]], filename: str) -> None:
    if not board:
        print("No board generated to save.")
        return
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for row in board:
                line = ",".join(str(x) for x in row)
                f.write(line + "\n")
    except OSError as e:
        print(f"Error! Could not save to '{filename}': {e}")

def main() -> None:
    print("Program starting.")
    board: list[list[int]] = []

    while True:
        print()
        print_menu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            try:
                rows_raw = input("Insert rows: ").strip()
                cols_raw = input("Insert columns: ").strip()
                mines_raw = input("Insert mines: ").strip()
                rows = int(rows_raw)
                cols = int(cols_raw)
                mines = int(mines_raw)

                generateMinefield(board, rows, cols, mines)
            except ValueError as e:
                print(e)

        elif choice == "2":
            show_board(board)

        elif choice == "3":
            if not board:
                print("No board generated to save.")
            else:
                fname = input("Insert filename: ").strip()
                if fname == "":
                    print("Invalid filename.")
                else:
                    save_board(board, fname)

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Unknown option!")

    print()
    print("Program ending.")

if __name__ == "__main__":
    main()
