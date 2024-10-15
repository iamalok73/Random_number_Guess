import random

def number_guessing_game():
   
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100.")

    while not guessed:
        try:
           
            user_guess = int(input("Enter your guess: "))
            attempts += 1

           
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
if __name__ == "__main__":
    number_guessing_game()
