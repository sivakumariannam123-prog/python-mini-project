def validate_password(password):
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_number = any(char.isdigit() for char in password)
    valid_length = 6 <= len(password) <= 12

    if valid_length and has_lowercase and has_uppercase and has_number:
        return True
    return False


password = input("Enter your password: ")

if validate_password(password):
    print("Valid Password")
else:
    print("Invalid Password")

    if len(password) < 6:
        print("- Password must contain at least 6 characters.")
    elif len(password) > 12:
        print("- Password must contain at most 12 characters.")

    if not any(char.islower() for char in password):
        print("- Password must contain a lowercase letter.")

    if not any(char.isupper() for char in password):
        print("- Password must contain an uppercase letter.")

    if not any(char.isdigit() for char in password):
        print("- Password must contain a number.")