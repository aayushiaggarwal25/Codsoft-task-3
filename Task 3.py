
import random

# Character sets we can mix together to build a password
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()_-+=?"


def get_length():
    """Keep asking until the user enters a valid positive whole number."""
    while True:
        value = input("How many characters should the password be? ")
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a positive whole number.")


def get_yes_no(question):
    """Ask a yes/no question and keep asking until we get a clear answer."""
    while True:
        answer = input(question + " (y/n): ").lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        print("Please type 'y' or 'n'.")


def generate_password(length, use_upper, use_digits, use_symbols):
    # Start with lowercase letters always included
    character_pool = LOWERCASE

    if use_upper:
        character_pool += UPPERCASE
    if use_digits:
        character_pool += DIGITS
    if use_symbols:
        character_pool += SYMBOLS

    # Build the password one character at a time
    password = ""
    for i in range(length):
        random_character = random.choice(character_pool)
        password += random_character

    return password


def main():
    print("Welcome to the Simple Password Generator!")
    print("Let's set up your password options.\n")

    length = get_length()
    use_upper = get_yes_no("Include uppercase letters?")
    use_digits = get_yes_no("Include numbers?")
    use_symbols = get_yes_no("Include symbols (!@#$ etc.)?")

    password = generate_password(length, use_upper, use_digits, use_symbols)

    print("\nHere is your generated password:")
    print(password)


# This makes sure the program runs only when this file is executed directly
if __name__ == "__main__":
    main()