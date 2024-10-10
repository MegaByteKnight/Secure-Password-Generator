import random
import string

def generate_password(length):
    """
    Generates a secure password of specified length.
    The password includes at least one uppercase letter,
    one lowercase letter, one digit, and one special character.
    
    Args:
        length (int): The total length of the password (minimum 4).
        
    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Character categories
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice('!@#$%^&*()-_=+[]{}|;:,.<>?/')

    # Combine all characters
    all_chars = string.ascii_letters + string.digits + '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    # Generate random characters to fill the rest of the password length
    remaining_length = length - 4
    if remaining_length > 0:
        remaining_chars = random.choices(all_chars, k=remaining_length)
    else:
        remaining_chars = []

    # Combine all parts of the password
    password_list = [uppercase, lowercase, digit, special] + remaining_chars

    # Shuffle the list to ensure randomness
    random.shuffle(password_list)

    # Convert the list to a string to form the final password
    password = ''.join(password_list)
    return password

def calculate_strength(password):
    """
    Calculates the strength of the password.
    
    Args:
        password (str): The password to evaluate.
        
    Returns:
        str: A string indicating the strength level.
    """
    length = len(password)
    categories = 0

    if any(c.islower() for c in password):
        categories += 1
    if any(c.isupper() for c in password):
        categories += 1
    if any(c.isdigit() for c in password):
        categories += 1
    if any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in password):
        categories += 1

    # Simple strength evaluation logic
    if length >= 12 and categories == 4:
        return 'Very Strong'
    elif length >= 8 and categories >= 3:
        return 'Strong'
    elif length >= 6 and categories >= 2:
        return 'Medium'
    else:
        return 'Weak'

if __name__ == "__main__":
    print("Welcome to the Secure Password Generator!")
    try:
        length_input = input("Enter the desired password length (minimum 4): ")
        length = int(length_input)

        password = generate_password(length)
        strength = calculate_strength(password)

        print(f"\nGenerated Password: {password}")
        print(f"Password Strength: {strength}")

    except ValueError as ve:
        print(f"Error: {ve}")
