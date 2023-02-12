import random

def get_user_input():
    user_input = input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: ")
    try:
        user_input = int(user_input)
        if user_input not in [1, 2, 3]:
            raise ValueError("Invalid input. Please enter either 1, 2, or 3.")
    except ValueError as error:
        print(error)
        return get_user_input()
    return user_input

def determine_result(user_input, computer_input):
    options = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"You chose {options[user_input]}, computer chose {options[computer_input]}.")
    if user_input == computer_input:
        return "Tie"
    elif (user_input == 1 and computer_input == 3) or (user_input == 2 and computer_input == 1) or (user_input == 3 and computer_input == 2):
        return "You win"
    else:
        return "Computer wins"

print("Welcome to Rock-Paper-Scissors!")
user_input = get_user_input()
computer_input = random.randint(1, 3)
result = determine_result(user_input, computer_input)
print(f"Result: {result}.")
