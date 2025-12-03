from template import add, subtract, divide, multiply               

def showOptions() -> None:                                        
    """Näyttää käyttäjälle valikkokohdat."""
    print("\nCalculator Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:                                           
    """Kysyy käyttäjältä valikon valinnan."""
    while True:                                                   
        try:
            choice = int(input("Your choice: "))                  
            
            if choice in [0, 1, 2, 3, 4]:                        
                return choice                                     
            
            print("Invalid choice. Please select 0-4.")          
        
        except ValueError:
            print("Invalid input. Please enter a number.")                                        
        
        except (KeyboardInterrupt, EOFError):                     
            print("\nUser interrupted. Exiting...")
            return 0                                              

def askValue(PPrompt: str) -> float:                              
    """Kysyy käyttäjältä liukulukuarvon."""
    while True:                                                   
        try:
            value = float(input(PPrompt))                         
            return value                                  
        except ValueError:                    
            print("Invalid input. Please enter a valid number.")
        
        except (KeyboardInterrupt, EOFError):                 
            print("\nUser interrupted. Returning to menu.")
            return None                                        

def main() -> None:                                 
    """Pääohjelma joka pyörittää laskinta."""
    print("Program starting.")
    print("Calculator - Basic Arithmetic Operations")
    
    while True:                                                   
        showOptions()                                             
        choice = askChoice()                                      
        
        if choice == 0:                                           
            print("Exiting calculator...")
            print("Program ending.")
            break                                                 

        
        value1 = askValue("Enter first value: ")                  
        if value1 is None:                                        
            continue                                             
        value2 = askValue("Enter second value: ")               
        if value2 is None:                            
            continue                             
        
        try:
            if choice == 1:                                    
                result = add(value1, value2)                
                print(f"Result: {value1} + {value2} = {result}")
            
            elif choice == 2:                                
                result = subtract(value1, value2)            
                print(f"Result: {value1} - {value2} = {result}")
            
            elif choice == 3:                                  
                result = multiply(value1, value2)              
                print(f"Result: {value1} * {value2} = {result}")
            
            elif choice == 4:                                
                result = divide(value1, value2)              
                print(f"Result: {value1} / {value2} = {result}")
        
        except ZeroDivisionError as e:                       
            print(f"Error: {e}")                             

if __name__ == "__main__":                          
    main()                       
