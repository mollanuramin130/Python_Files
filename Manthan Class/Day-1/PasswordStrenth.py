import re

def is_strong_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False

    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]', password):
        return False

    # If all checks pass, the password is strong
    return True

# Input a password from the user
password = input("Enter a password: ")

# Check if the password is strong
if is_strong_password(password):
    print("Password is strong.")
else:
    print("Password is weak. Please use a stronger password.")
