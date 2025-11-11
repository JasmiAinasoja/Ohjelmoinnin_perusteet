import codecs

def collect_input() -> list:
    print("Collecting plain text rows for ciphering.")
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        rows.append(row)
    return rows

def rot13_cipher(text: str) -> str:
    return codecs.encode(text, 'rot_13')

def cipher_rows(rows: list) -> list:
    return [rot13_cipher(row) for row in rows]

def display_ciphered(rows: list):
    print("\n#### Ciphered text ####")
    for row in rows:
        print(row)

def save_ciphered(rows: list):
    print("\n#### Ciphered text ####")
    filename = input("Insert filename to save: ")
    if filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
        return
    with open(filename, "w") as f:
        for row in rows:
            f.write(row + "\n")
    print("Ciphered text saved!")
    

def main():
    print("Program starting.\n")
    plain_rows = collect_input()
    ciphered_rows = cipher_rows(plain_rows)

    display_ciphered(ciphered_rows)
    save_ciphered(ciphered_rows)

    print("Program ending.")

if __name__ == "__main__":
    main()