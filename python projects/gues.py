import random

def guess():
    number = random.randint(1,100)
    attempts = 0 
    print("gues the number between 1 and 100!")

    while(True):
            user = input("gues a number between 1, 100: ")
            if user == "stop":
                 break
            try:   
                user = int(user)
                attempts += 1 
                if user < number:
                    print("higher")
                elif user > number:
                    print("lower")
                elif user == number:
                    print(f"you got it in {attempts} attempts")
                    break
            except ValueError:
                print("only use numbers. if you want to stop type 'stop'")
            
guess()


        

