def frameWord(Pword):
    print("*" * (len(Pword)+4))
    print(f"* {Pword} *")
    print("*" * (len(Pword)+4))
    return None
          
def main():
    print("Program starting.")
    word = input("Insert word: ")
    frameWord(word)
    print("\nProgram ending.")
    return None

main()