# Password Generator and Strength Checker

This Python script is a versatile tool for generating and evaluating passwords. It provides options for automatically generating random passwords, creating custom passwords based on user-defined criteria, and checking the strength of any given password. The script uses the `zxcvbn` library to evaluate password strength and the `prettytable` library to display options and results in a tabular format.

## Features

1. **Automatic Password Generation**: Generates a random password of specified length using uppercase letters, lowercase letters, digits, and symbols.
2. **Custom Password Generation**: Allows the user to specify which character sets (uppercase, lowercase, digits, symbols) to include in the generated password.
3. **Password Strength Checker**: Evaluates the strength of a user-provided password or the generated password using the `zxcvbn` library.

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

   Execute the script using Python along with the desired command-line arguments:

   ```bash
   python password_generator.py [options]
   ```

### Command-Line Options

The script accepts the following command-line options:

- `-l`, `--length`: Length of the password (default is 12).
- `-a`, `--auto`: Generate password automatically.
- `-cu`, `--custom`: For custom password generation.
- `-u`, `--upper`: Include uppercase letters in the custom password.
- `-lo`, `--lower`: Include lowercase letters in the custom password.
- `-s`, `--symbols`: Include symbols in the custom password.
- `-d`, `--digits`: Include digits in the custom password.
- `-c`, `--check`: Check the strength of the generated or given password.
- `-gp`, `--given_password`: Checks user-given password instead of the generated one.

### Examples

1. **Automatic Password Generation**

   To generate a password automatically with the default length of 12:

   ```bash
   python password_generator.py --auto
   ```

   To generate an automatic password of a specific length (e.g., 16):

   ```bash
   python password_generator.py --auto --length 16
   ```

2. **Custom Password Generation**

   To generate a custom password including uppercase letters, digits, and symbols:

   ```bash
   python password_generator.py --custom --upper --digits --symbols
   ```

   To generate a custom password of a specific length (e.g., 10) including all character types:

   ```bash
   python password_generator.py --custom --length 10 --upper --lower --digits --symbols
   ```

3. **Password Strength Checking**

   To check the strength of a generated password:

   ```bash
   python password_generator.py --auto --check
   ```

   To check the strength of a user-given password:

   ```bash
   python password_generator.py --check --given_password
   ```

   You will be prompted to enter the password securely.

### Example Output

The script outputs the generated password and its strength in a tabular format. For example:

```plaintext
+----+---------------------+-----------------+
| No |     Description     |      Output     |
+----+---------------------+-----------------+
| 1  | Generated Password  | ************    |
| 2  | Strength of Password| Strong          |
+----+---------------------+-----------------+
```

---

Feel free to fork this repository, report issues, and contribute to its development. Happy password generating!
