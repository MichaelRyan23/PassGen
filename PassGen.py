import random
import string

def generate_password(length):
    if length > 25 or length < 1:
        raise ValueError("Password length must be between 1 and 25 characters.")
    
    # Define possible character sets
    letters = string.ascii_letters  # Uppercase and lowercase letters
    digits = string.digits  # Numbers
    special_characters = "!@#$%^&*()_+{}[]<>?~"  # Special characters

    # Combine all characters
    all_characters = letters + digits + special_characters

    # Ensure the password includes at least one letter, digit, and special character
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill remaining characters randomly
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle to randomize the character order
    random.shuffle(password)

    return ''.join(password)

# Get user input
try:
    user_input = int(input("Enter the desired password length (1 to 25): "))
    password = generate_password(user_input)
    print(f"Generated Password: {password}")
except ValueError as e:
    print(f"Error: {e}")
