# Poistumiskoodiharjoitus
# sys.exit(0) -> ohjelma päättyi onnistuneesti
# Ohjelman kaatuessa, koodi järjestelmälle voi olla 1-255
# sys.exit(1)
# sys.exit()

import sys

def main() -> None:

    print("Program starting.")

    
    Feed = input("Insert exit code (0-255): ")
    ExitCode = int(Feed)
    if ExitCode == 0:
        print("Clean exit.")
    else:
        print("Error code.")
    sys.exit(ExitCode)
    print("Program ending.")
    return None

main()
# write echo "$?" to get exit code
