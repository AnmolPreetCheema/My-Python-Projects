import random

def guess_the_number():

    print("I have chosen a number between 1 and 100. Try to guess it!")

    secret_number = random.randint(1, 100)  
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low")
            elif guess > secret_number:
                print("Too high")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break  
        except ValueError:
            print("Please enter a valid number!")

    print("Thanks for playing")

# Run the game
guess_the_number()

