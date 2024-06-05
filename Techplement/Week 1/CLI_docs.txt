# Password Generator and Strength Checker

This Python script is a comprehensive tool for generating and evaluating passwords. It provides options for automatically generating random passwords, creating custom passwords based on user-defined criteria, and checking the strength of any given password. The script uses the `zxcvbn` library to evaluate password strength and the `prettytable` library to display options and results in a tabular format.

## Features

1. **Automatic Password Generation**: Generates a random password of specified length using uppercase letters, lowercase letters, digits, and symbols.
2. **Custom Password Generation**: Allows the user to specify which character sets (uppercase, lowercase, digits, symbols) to include in the generated password.
3. **Password Strength Checker**: Evaluates the strength of a user-provided password using the `zxcvbn` library.

## Installation

To use this script, you need to have Python installed along with the following libraries:

- `zxcvbn`: For password strength evaluation.
- `prettytable`: For displaying tables in the console.

You can install these libraries using `pip`:

```bash
pip install zxcvbn prettytable
```

## Usage

1. **Clone the Repository or Download the Script**

   First, clone the repository to your local machine or download the script file directly.

   ```bash
   git clone https://github.com/your-repo/password-generator.git
   cd password-generator
   ```

2. **Run the Script**

   Execute the script using Python:

   ```bash
   python password_generator.py
   ```

3. **Interact with the Menu**

   The script presents a menu with the following options:

   ```
   +----+-----------------------+
   | No |        Options        |
   +----+-----------------------+
   |  1 | Automatic             |
   |  2 | Custom                |
   |  3 | Check your password   |
   |  4 | Exit                  |
   +----+-----------------------+
   ```

   Choose an option by entering the corresponding number.

### Detailed Steps

1. **Automatic Password Generation**

   - Select option `1` for automatic password generation.
   - Enter the desired length of the password when prompted. The password must be at least 8 characters long.
   - The script will generate a random password using uppercase letters, lowercase letters, digits, and symbols.
   - The generated password and its strength will be displayed.

   Example:

   ```plaintext
   Choose from above options: 1
   Enter the length of password: 12
   Generated Password: ************
   Strength of Password: Strong
   ```

2. **Custom Password Generation**

   - Select option `2` for custom password generation.
   - Enter the desired length of the password when prompted. The password must be at least 8 characters long.
   - Specify which character sets to include in the password by responding with `y` (yes) or `n` (no) to the following prompts:
     - Uppercase letters
     - Lowercase letters
     - Symbols
     - Digits
   - The script will generate a password based on the selected criteria.
   - The generated password and its strength will be displayed.

   Example:

   ```plaintext
   Choose from above options: 2
   Enter the length of password: 10
   If you want UPPER CASE letters press (y/n): y
   If you want lower case letters press (y/n): y
   If you want symbols letters press (y/n): n
   If you want digits letters press (y/n): y
   Custom Password: **********
   Strength of Password: Fair
   ```

3. **Check Your Password**

   - Select option `3` to check the strength of a given password.
   - Enter your password when prompted. For security, the input will be hidden.
   - The script will evaluate and display the strength of the entered password.

   Example:

   ```plaintext
   Choose from above options: 3
   Enter your password: ********
   Strength of given Password: Weak
   ```

4. **Exit**

   - Select option `4` to exit the script.

---

Feel free to fork this repository, report issues, and contribute to its development. Happy password generating!
