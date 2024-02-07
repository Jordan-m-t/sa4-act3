number = 10
max_guesses = 3
current_guess = 0

print("I'm thinking of a number...")

while current_guess < max_guesses:
    guess_input = input(f"What number am I thinking of? (Enter 'q' to quit) You have {max_guesses - current_guess} guesses left: ")
    
    if guess_input.lower() == 'q':
        print(f"The number was {number}.")
        break
    
    try:
        guess = int(guess_input)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'q' to quit.")
        continue
    
    current_guess += 1
    
    if guess == number:
        print(f"Congrats! You guessed the right number in {current_guess} attempts.")
        break
    elif current_guess < max_guesses:
        if guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print(f"Sorry, you've run out of guesses. The correct number was {number}.")
