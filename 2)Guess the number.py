import random

def guess_the_number():
  number = random.randint(1, 100)
  print("Number has been generated. You have 10 turns to guess the number.")
  for i in range(10):
    try:
      user_guess = int(input("Enter your guess: "))
      if user_guess == number:
        print("Congratulations! You have guessed the number.")
        return
      elif user_guess < number:
        print("The number is higher.")
      else:
        print("The number is lower.")
    except ValueError:
      print("Invalid input. Please enter a number.")
  print(f"You have exhausted all your turns. The number was {number}.")

def computer_guess_the_number():
  number = random.randint(1, 100)
  print("Number has been generated. The computer will have 10 turns to guess the number.")
  low, high = 1, 100
  for i in range(10):
    computer_guess = (low + high) // 2
    print(f"The computer's guess is: {computer_guess}")
    if computer_guess == number:
      print("The computer has guessed the number.")
      return
    elif computer_guess < number:
      low = computer_guess + 1
    else:
      high = computer_guess - 1
  print(f"The computer has exhausted all its turns. The number was {number}.")

def main():
  print("Welcome to the Number Guessing Game!")
  choice = input("Do you want to guess the number (1) or do you want the computer to guess the number (2)? ")
  if choice == '1':
    guess_the_number()
  elif choice == '2':
    computer_guess_the_number()
  else:
    print("Invalid choice. Please try again.")

if __name__ == '__main__':
  main()
