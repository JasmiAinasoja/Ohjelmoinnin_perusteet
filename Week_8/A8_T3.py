from template import askChoice, showMenu          

def readValues(filename: str):                                     
    values = []                                          
    try:                                                        
        with open(filename, "r", encoding="UTF-8") as f:          
            for line in f:                                        
                line = line.strip()                                 

                if line:                                         
                    try:                                           
                        values.append(float(line))           

                    except ValueError:                          
                        print(f"Skipping invalid value: {line}")   

                    except (KeyboardInterrupt, EOFError):       
                        print("User interrupted. Cancelling.")    
                        break                                

        print(f"File '{filename}' read successfully.\n")         

    except FileNotFoundError:                                      
        print(f"Error: File '{filename}' not found.\n")      

    except (KeyboardInterrupt, EOFError):                           
        print("User interrupted. Cancelling.")               
    
    return values                                            

def calculateSum(values: list[float]):                          
    return round(sum(values))                                   

def calculateAverage(values: list[float]):                       
    if len(values) == 0:                                         
        print("Error: No values loaded.\n")                    
        return 0.0                                               
    
    return round(sum(values) / len(values), 1)                    

def processChoice(choice: int, values: list[float]):            
    if choice == 0:                                              
        return False                                            

    elif choice == 1:                                           
        filename = input("Insert filename: ").strip()             
        new_values = readValues(filename)                         
        if new_values:                                          
            values.extend(new_values)                            

    elif choice == 2:                                              
        print(f"Amount of values: {len(values)}\n")              

    elif choice == 3:                                              
        if not values:                                            
            print("Error: No values loaded.\n")                    
        else:                                                       
            print(f"Sum of values: {calculateSum(values)}\n")      

    elif choice == 4:                                             
        if not values:                                            
            print("Error: No values loaded.\n")                   
        else:                                                      
            print(f"Average of values: {calculateAverage(values)}\n") 
    
    return True                                                   


options = [
    "1 - Read values",                                              
    "2 - Amount of values",                                      
    "3 - Calculate sum of values",                                  
    "4 - Calculate average of values",                             
    "0 - Exit"                                                    
]

def main():                                                 
    print("Program starting.")                                  

    values: list[float] = []                                   

    while True:                                                     
        showMenu(options)                                         

        choice = askChoice([0, 1, 2, 3, 4])                     

        if not processChoice(choice, values):              
            break                                               

    print("Program ending.")                                     

if __name__ == "__main__":                                 
    main()