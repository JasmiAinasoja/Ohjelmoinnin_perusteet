########################################################
# Task A9_T2
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################


import sys

def main():
    print("Program starting.")
    try:
        code = int(input("Insert exit code(0-255): "))
        if 0 <= code <= 255:
            print("Clean exit")
            sys.exit(code)
        else:
            print("Error code")
            sys.exit(1)
    except ValueError:
        print("Error code")
        sys.exit(1)

if __name__ == "__main__":
    main()
