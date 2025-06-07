import random

def dice():
    while(True):
        roll = input("Type 'roll' to roll, or 'quit' to exit: ")
        if roll == "quit":
            break
        elif roll == "exit":
            break 

        else:
           number1 = random.randint(1, 6) 
           number2 = random.randint(1, 6) 
           awnser = number1 + number2

           print(f"you rolled a {number1} and a {number2} total: {awnser}")  
dice()
            
    