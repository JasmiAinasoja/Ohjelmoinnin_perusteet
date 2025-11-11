def main():
    print("Program starting.")
    print("This program can copy a file.")

    source_file = input("Insert source filename: ")
    destination_file = input("Insert destination filename: ")

    print(f"Reading file '{source_file}' content.")
    with open(source_file, "r", encoding="UTF-8") as f:         
        content = f.read()                                      
    print("File content ready in memory.")

    print(f"Writing content into file '{destination_file}'.")
    with open(destination_file, "w", encoding="UTF-8") as f:    
        f.write(content)                                        
    print("Copying operation complete.")

    print("Program ending.")

if __name__ == "__main__":
    main()