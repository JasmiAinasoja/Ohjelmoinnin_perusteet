
from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle, Polygon
def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    x = float(input("- Left edge position: "))
    y = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill_color = input("- Fill color: ")
    stroke_color = input("- Stroke color: ")

    square = Rect(insert=(x, y),
                  size=(side, side),
                  fill=fill_color,
                  stroke=stroke_color)
    PDwg.add(square)
    print()

def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    cx = float(input("- Center X coord: "))
    cy = float(input("- Center Y coord: "))
    r = float(input("- Radius: "))
    fill_color = input("- Fill color: ")
    stroke_color = input("- Stroke color: ")

    circle = Circle(center=(cx, cy),
                    r=r,
                    fill=fill_color,
                    stroke=stroke_color)
    PDwg.add(circle)
    print()

def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ").strip()
    print(f'Saving file to "{filename}"')
    confirm = input("Proceed (y/n)?: ").strip().lower()
    if confirm == 'y':
        PDwg.saveas(filename, pretty=True, indent=2)
        print("Vector saved successfully!\n")
    else:
        print("Save operation cancelled.\n")


def main() -> None:
    print("Program starting.")
    Dwg = Drawing(size=("500px", "500px"))

    while True:
        print("Options:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Save svg")
        print("0 - Exit")
        choice = input("Your choice: ").strip()

        if choice == '1':
            drawSquare(Dwg)
        elif choice == '2':
            drawCircle(Dwg)
        elif choice == '3':
            saveSvg(Dwg)
        elif choice == '0':
            print("Exiting program.\n")
            print("Program ending.")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
