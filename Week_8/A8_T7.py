import math
import svgwrite

def calculate_hexagon_points(cx, cy, apothem):
    circumradius = apothem / math.cos(math.radians(30))
    
    points = []
    angles = [30, 90, 150, 210, 270, 330] 
    for angle in angles:
        x = cx + circumradius * math.cos(math.radians(angle))
        y = cy - circumradius * math.sin(math.radians(angle))
        points.append((round(x), round(y)))
    return points

def draw_square(dwg, cx, cy, size, fill, stroke):
    half = size / 2
    rect = dwg.rect(insert=(cx - half, cy - half), size=(size, size),
                    fill=fill, stroke=stroke)
    dwg.add(rect)

def draw_circle(dwg, cx, cy, radius, fill, stroke):
    circle = dwg.circle(center=(cx, cy), r=radius, fill=fill, stroke=stroke)
    dwg.add(circle)

def draw_hexagon(dwg, cx, cy, apothem, fill, stroke):
    points = calculate_hexagon_points(cx, cy, apothem)
    hexagon = dwg.polygon(points=points, fill=fill, stroke=stroke)
    dwg.add(hexagon)

def main():
    print("Program starting.")
    dwg = svgwrite.Drawing(size=("500px", "500px"))
    
    while True:
        print("\nOptions:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Draw hexagon")
        print("4 - Save svg")
        print("0 - Exit")
        choice = input("Your choice: ")
        
        if choice == "1":
            cx = int(input("Center X: "))
            cy = int(input("Center Y: "))
            size = int(input("Square size: "))
            fill = input("Insert fill: ")
            stroke = input("Insert stroke: ")
            draw_square(dwg, cx, cy, size, fill, stroke)
        
        elif choice == "2":
            cx = int(input("Center X: "))
            cy = int(input("Center Y: "))
            radius = int(input("Circle radius: "))
            fill = input("Insert fill: ")
            stroke = input("Insert stroke: ")
            draw_circle(dwg, cx, cy, radius, fill, stroke)
        
        elif choice == "3":
            print("Insert hexagon details:")
            cx = int(input("Middle point X: "))
            cy = int(input("Middle point Y: "))
            apothem = int(input("Apothem length: "))
            fill = input("Insert fill: ")
            stroke = input("Insert stroke: ")
            draw_hexagon(dwg, cx, cy, apothem, fill, stroke)
        
        elif choice == "4":
            filename = input("Insert filename: ")
            confirm = input(f'Saving file to "{filename}"\nProceed (y/n)?: ')
            if confirm.lower() == 'y':
                dwg.saveas(filename)
                print("Vector saved successfully!")
        
        elif choice == "0":
            print("Exiting program.\nProgram ending.")
            break
        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
