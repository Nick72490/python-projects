print("even or odd")
number = input("enter a number:")

number = int(number)

def number_checker(number):
    if number % 2 == 0:
        print("even") 
    else:
        print("odd")

number_checker(number)