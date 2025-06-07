import random
score_user = 0
score_computer = 0

def game():

    while(True):
     
     global score_user 
     global score_computer 

     print(f"score user: {score_user}")
     print(f"score computer: {score_computer}")
         
     print("1.rock")
     print("2.scissors")
     print("3.paper")
     print("4.quit")
     user_choice = input("number :")
     if user_choice == "4":
        break

     options = ["rock", "scissors", "paper", "quit"]
     user_choice_word = options[int(user_choice) - 1]  # Convert "1" to index 0, etc.
     
     options = ["rock", "paper", "scissors"]
     computer_choice = random.choice(options)

     print(f"user choice: {user_choice_word} ")
     print(f"Computer chose: {computer_choice}")

     if user_choice_word == computer_choice:
         print("It's a tie!")
     elif (user_choice == "1" and computer_choice == "scissors") or \
          (user_choice == "2" and computer_choice == "paper") or \
          (user_choice == "3" and computer_choice == "rock"):
         print("You win!")
         score_user += 1
     else:
         print("Computer wins!")
         score_computer += 1 
game()



