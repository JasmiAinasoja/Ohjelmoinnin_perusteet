print("Program starting.\n")

Feed = input("Insert starting point: ")
PointStart = int(Feed)
Feed = input("Insert stopping point: ")
PointStop = int(Feed)
Feed = input("Insert inspection point: ")
PointInspect = int(Feed)

Run = True

if(PointStart >= PointStop):
    print("Starting point value must be less than the stopping point value.")
    Run = False
if((PointStart > PointInspect) or (PointInspect > PointStop)):
    print("Inspection value must be within the range of start and stop.")
    Run = False

if(Run):
    print("First loop - inspection with break:")
    for i in range(PointStart, PointStop):
        if(i == PointInspect):
            break
        else:
            print(f"{i}", end=' ')

    print() #tyhjä rivi

    print("Second loop - inspection with continue:")
    for i in range(PointStart, PointStop):
        if(i == PointInspect):
            continue
        else:
            if(i == (PointStop-1)):
                print(i)
            else:
                print(i, end=' ')


print("\nProgram ending.")