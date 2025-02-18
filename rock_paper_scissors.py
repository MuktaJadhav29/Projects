import random
user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"] 

while (user_wins < 3 and computer_wins < 3):
    
    user_input = input("Type rock/paper/scissors or 4 to quit:").lower()
    
    if user_input == "4":
        break
    
    if user_input not in options:
        continue
     
    random_number = random.randint(0,2)
    computer_move = options[random_number]
    print(f"computer picked {computer_move}.")
    
    if user_input == "rock" and computer_move == "scissors":
        print("You win!")
        user_wins += 1
    
    elif user_input == "paper" and computer_move == "rock":
        print("You win!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_move == "paper":
        print("You win!")
        user_wins += 1 
    
    elif user_input == computer_move:
        print("there's a tie")
    
    else: 
        print("you lose")
        computer_wins += 1 
    
    print(f"you won {user_wins} times and you lost {computer_wins} times")
    