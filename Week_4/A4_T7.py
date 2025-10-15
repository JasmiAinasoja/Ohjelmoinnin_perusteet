print("Program starting.\n")
print("Check multiplicative persistence.")

num = int(input("Insert an integer: "))

steps = 0
while num >= 10:
        luvut = [int(d) for d in str(num)]
        tulo = 1
        kaava = ""
        
        for i, d in enumerate(luvut):
                tulo *= d
                kaava += str(d)
                if i < len(luvut) - 1:
                        kaava += " * "
        
        print(f"{kaava} = {tulo}")
        num = tulo
        steps += 1
print("No more steps.")
print(f"\nThis program took {steps} step(s)")
print("\nProgram ending.")