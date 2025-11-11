def readFile(Filename):
    Filehandler = open(Filename, 'r')
    Content = ''
    Row = Filehandler.readline()
    while Row !='':
        Content += Row
        Row = Filehandler.readline()
    Filehandler.close()
    return Content # Palaa takaisin kutsukohtaan

def main():
    print("Program starting.")
    print("This program can read a file.")
    Filename = input("Insert filename: ")
    FileContent = readFile(Filename) # Hyppää readFile funktioon
    print(f'#### START "{Filename}" ####')
    print(FileContent)
    print(f'#### END "{Filename}" ####')
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()