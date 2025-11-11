def writeFile(PFilename, PContent):
    Filehandle = open(PFilename, 'w')
    Filehandle.write(PContent)
    Filehandle.close()
    return None

def main():
    print("Program starting.")
    FirstName = input("Insert first name: ")
    LastName = input("Insert last name: ")
    Filename = input("Insert filename: ")
    Content = "{}\n{}".format(FirstName,LastName)
    writeFile(Filename, Content)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()