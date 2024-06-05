import random
from zxcvbn import zxcvbn
import string
from prettytable import PrettyTable
import getpass

upper_char = string.ascii_uppercase
lower_char = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

def auto_generator(length):
  res1 = ""

  for i in range(length):
    all_char = upper_char+lower_char+symbols+digits
    password = random.choice(all_char)
    res1 += password
  return res1



def custom_generator(length):
  res2 = ""
  Upper = input("If want UPPER CASE letters press (y/n):- ")
  Lower = input("If want lower case letters press (y/n):- ")
  Symbols = input("If want symbols  letters press (y/n):- ")
  Digits = input("If want digits letters press (y/n):- ")

  custom = ""
  if Upper == "y":
    custom += upper_char
  if Lower == "y":
    custom += lower_char
  if Symbols == "y":
    custom += symbols
  if Digits == "y":
    custom += digits

  if not custom:
    print("No character chosen")
  else:
    for i in range(length):
      password = random.choice(custom)
      res2 += password
    return res2

def Pass_Checker(password):
  result = zxcvbn(password)
  score = result['score']
  strength = ["Very Weak", "Weak", "Fair", "Strong", "Very Strong"]  
  return strength[score]



def main():
  menu = PrettyTable()

  menu.field_names = ["No","Options"]
  menu.add_row(["1","Automatic"])
  menu.add_row(["2","Custom"])
  menu.add_row(["3","check your password"])
  menu.add_row(["4","exit"])

  show = PrettyTable()
  show.field_names = ["No.","Text","Output"]

  while True:
    print(menu)
    choice = int(input("Chose from above options:- "))
    match choice:
      case 1:
        length = int(input("Enter the range of password:- "))
        if length <8:
          break
        else:
          password = auto_generator(length)
          strength = Pass_Checker(password)
          show.add_row(["1","Generated Password",password])
          show.add_row(["2","Strength of Password",strength])
          print(f"Generated Pasword:- {password}")
      case 2:
        length = int(input("Enter the range of password:- "))
        if length < 8:
          break
        else:
          password = custom_generator(length)
          strength = Pass_Checker(password)
          show.add_row(["1","Generated Password",password])
          show.add_row(["2","Strength of Password",strength])
          print(f"Custom Password:- {password}")
      case 3:
        check = getpass.getpass(prompt="Enter your password:- ")
        strength = Pass_Checker(check)
        show.add_row(["1.","Strength of given Password",strength])
      case 4:
        print("Exiting Password Generator!")
        break
      case _:
        print("Invalid choice!")
        break

    print(show)
    choi2 = input("If you want to generate password again press (y/n) - ")
    if choi2 == "y":
      continue
    elif choi2 == "n":
      break

if __name__ == "__main__":
  main()