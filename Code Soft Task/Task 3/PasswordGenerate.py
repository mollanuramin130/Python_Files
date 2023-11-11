import random
import string

def generate_password(length):
    # Define character sets for the password
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on desired complexity
    if length < 8:
        # Use only lowercase and digits for short passwords
        chars = lowercase_chars + digits
    elif length < 12:
        # Include uppercase, lowercase, and digits for medium-length passwords
        chars = lowercase_chars + uppercase_chars + digits
    else:
        # Include uppercase, lowercase, digits, and special characters for long passwords
        chars = lowercase_chars + uppercase_chars + digits + special_chars

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
