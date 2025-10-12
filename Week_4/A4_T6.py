print("Program starting.")

num = int(input("Insert a positive integer: "))
steps = 0
print(f"{num}", end="")

while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        print(f" -> {num}", end="")
        steps += 1

print(f"\nSequence had {steps} total steps.")

print("\nProgram ending.")