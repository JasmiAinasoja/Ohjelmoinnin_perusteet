print("Program starting.\n")

WordCount = 0
CharCount = 0

Word = input("Insert word (empty stops): ")
while Word != '':
    WordCount += 1
    CharCount += len(Word)
    Word = input("Insert word (empty stops): ")

print("\nYou inserted:")
print(f"- {WordCount} words")
print(f"- {CharCount} characters")

print("\nProgram ending.")