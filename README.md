# Secure Password Generator

A simple yet secure password generator implemented in Python. This tool generates passwords that include uppercase letters, lowercase letters, digits, and special characters, ensuring strong password creation. It also evaluates the strength of the generated password.

## Features

- **User-Friendly Input**: Only asks for the desired password length.
- **Comprehensive Character Inclusion**: Automatically includes at least one character from each category:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters
- **Password Strength Evaluation**: Provides an assessment of the password's strength based on length and character variety.
- **Randomized Output**: Shuffles characters to ensure password randomness and unpredictability.
- **Error Handling**: Gracefully handles invalid inputs with informative messages.

## How to Use

### Prerequisites

- Python 3.x installed on your system.
- Access to a command-line interface or terminal.

### Steps

1. **Clone the Repository**
   ```
   git clone https://github.com/MegaByteKnight/secure-password-generator.git
   cd secure-password-generator
   ```

2. **Run the Script**
   ```
   python password_generator.py
   ```

3. **Follow the On-Screen Prompts**
- Enter the desired password length when prompted (minimum length is 4).
- The script will generate a password and display its strength.

### Example
```
Welcome to the Secure Password Generator!
Enter the desired password length (minimum 4): 12

Generated Password: vI9;KdP!x2&Q
Password Strength: Very Strong
```
## Understanding the Password Strength Levels
- Very Strong: Password is 12 or more characters long and includes all four character types.
- Strong: Password is at least 8 characters long and includes at least three character types.
- Medium: Password is at least 6 characters long and includes at least two character types.
- Weak: Password does not meet the above criteria.

## Code Overview
The script consists of two main functions:
1. ```generate_password(length)```
- Validates the password length.
- Selects one character from each category to ensure inclusivity.
- Fills the rest of the password with random characters.
- Shuffles the characters to prevent patterns.
- Returns the generated password.

2. ```calculate_strength(password)```
- Checks for the presence of different character types.
- Determines the strength based on length and character variety.
- Returns the strength level as a string.

## Customization
- Adjust Character Sets
  - Modify the character sets in the ```generate_password``` function to include or exclude specific characters.
- Modify Strength Criteria
  - Adjust the conditions in the ```calculate_strength``` function to change how the strength is evaluated.

## Potential Enhancements
- GUI Version
  - Implement a graphical user interface using libraries like Tkinter for a more user-friendly experience.
- Save Passwords
  - Add functionality to save generated passwords to a secure file.
- Password Policies
  - Allow users to input custom password policies or complexity requirements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## Author
Brian Sawyer
