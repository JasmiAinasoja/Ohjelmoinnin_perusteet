import ts_lib as t1                                            
from template import askChoice, showMenu                       

options = [
    "1 - Calculate amount of timestamps during year",            
    "2 - Calculate amount of timestamps during month",           
    "3 - Calculate amount of timestamps during weekday",        
    "0 - Exit"                                                 
]

def processChoice(choice: int, timestamps):                      
    if choice == 0:                                            
        print("Exiting program.")                              
        return False                                             
    
    elif choice == 1:                                           
        try:
            year = int(input("Insert year: "))                 
            count = t1.calculateYears(year, timestamps)       
            print(f"Amount of timestamps during year '{year}' is {count}\n") 

        except ValueError:                                       
            print("Invalid input. Please insert a valid year.") 
        except (KeyboardInterrupt, EOFError):                   
            print("User interrupted. Cancelling.")             
            return False                                       
    
    elif choice == 2:                                           
        try:
            month = int(input("Insert month (1-12): "))          
            if not 1 <= month <= 12:                            
                print("Invalid month. Please enter 1-12.")       
                return True                                      
            count = t1.calculateMonths(month, timestamps)         
            print(f"Amount of timestamps during month '{month}' is {count}\n") 

        except ValueError:                                       
            print("Invalid input. Please insert a valid month (1-12).") 

        except (KeyboardInterrupt, EOFError):                    
            print("User interrupted. Cancelling.")              
            return False                                       
    
    elif choice == 3:                                          
        try:
            weekday = int(input("Insert weekday (1-7, Monday=1): "))
            if not 1 <= weekday <= 7:                           
                print("Invalid weekday. Please enter 1-7.")     
                return True                                       
            count = t1.calculateWeekdays(weekday, timestamps)    
            print(f"Amount of timestamps during weekday '{weekday}' is {count}\n") 

        except ValueError:                                      
            print("Invalid input. Please insert a valid weekday (1-7).") 

        except (KeyboardInterrupt, EOFError):                   
            print("User interrupted. Cancelling.")          
            return False                                        
    
    return True                                                  

def main():                                                     
    print("Program starting.")                               

    filename = input("Insert filename: ").strip()            

    timestamps = t1.readTimestamps(filename)                 

    while True:                                               
        showMenu(options)                                     

        choice = askChoice([0, 1, 2, 3])                   

        if not processChoice(choice, timestamps):                 
            break                                               

    print("Program ending.")                                  

if __name__ == "__main__":                                      
    main()