import random
import string

def generate_password(length, use_digits=True, use_special=True):
    letters = string.ascii_letters  # A-Z, a-z
    digits = string.digits if use_digits else ""
    special_chars = string.punctuation if use_special else ""

    all_chars = letters + digits + special_chars
    if not all_chars:
        return "Error: No characters available for password generation!"

    return ''.join(random.choice(all_chars) for _ in range(length))

print("Welcome to the Password Generator")

while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password should be at least 4 characters long!")
            continue

        use_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_digits, use_special)
        print(f"\nYour generated password: {password}")

    except ValueError:
        print("Please enter a valid number!")

    again = input("\nGenerate another password? (yes/no): ").lower()
    if again != 'yes':
        print("bye")
        break

