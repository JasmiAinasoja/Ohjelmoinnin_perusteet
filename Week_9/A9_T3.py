########################################################
# Task A9_T3
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################


import sys

def read_file_content(filename: str) -> str:
    """Read and return the content of a text file."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def main():
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    try:
        content = read_file_content(filename)
    except FileNotFoundError:
        print(f"Couldn't read file '{filename}'.")
        sys.exit(1)
    else:
        print(f"## {filename} ##")
        print(content, end="" if content.endswith("\n") else "\n")
        print(f"## {filename} ##")

    print("Program ending.")

if __name__ == "__main__":
    main()
