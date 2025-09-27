print("Program starting.")
print("Insert two integers.")
First = int(input("Insert first integer: "))
Second = int(input("Insert second integer: "))
sum = First + Second
Answer = sum % 2
print("Comparing inserted integers.")

if(First < Second):
    print("Second integer is greater.")
elif(First > Second):
    print("First integer is greater.")
else:
    print("Integers are the same.")

print("Adding integers together")
print(f"{First} + {Second} = {sum}")

print("Checking the parity of the sum...")
if Answer == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program is ending.")