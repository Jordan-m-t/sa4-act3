number = 10

print("I'm thinking of a number...")

while True:
    guess_input = input("What number am I thinking of? (Enter 'q' to quit) ")
    
    if guess_input.lower() == 'q':
        print(f"The number was {number}.")
        break
    
    try:
        guess = int(guess_input)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'q' to quit.")
        continue
    
    if guess == number:
        print("Congrats! You guessed the right number.")
    elif guess > number:
        print("Number was to high.")
    else:
        print("Number was to low.")
