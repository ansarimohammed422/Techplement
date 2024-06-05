import random
from zxcvbn import zxcvbn
import string
import argparse
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


def custom_generator(length,use_upper,use_lower,use_symbols,use_digits):
  res2 = ""

  custom = ""
  if use_upper:
    custom += upper_char
  if use_lower:
    custom += lower_char
  if use_symbols:
    custom += symbols
  if use_digits:
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
  parser = argparse.ArgumentParser(description = "Password Generator")
  parser.add_argument('-l','--length', type = int, default = 12, help = "Length of the Password (Default is 12)")
  parser.add_argument('-a', '--auto', action='store_true', help="Generate password automatically")
  parser.add_argument('-cu','--custom', action='store_true', help="For custom password generation")
  parser.add_argument('-u', '--upper', action='store_true', help="Include upper case letters")
  parser.add_argument('-lo', '--lower', action='store_true', help="Include lower case letters")
  parser.add_argument('-s', '--symbols', action='store_true', help="Include symbols")
  parser.add_argument('-d', '--digits', action='store_true', help="Include digits")
  parser.add_argument('-c', '--check', action = 'store_true', help="Checks Password Strength")
  parser.add_argument('-gp','--given_password', action='store_true', help="Checks user given password")
  args = parser.parse_args()
  show = PrettyTable()
  show.field_names = ["No.","Description","Output"]
  password = ""
  if args.auto:
    password = auto_generator(args.length)
    show.add_row(["1.","Generated Password",password])
  elif args.custom:
    password = custom_generator(args.length,args.upper,args.lower,args.symbols,args.digits)
    show.add_row(["1.","Generated Password",password])

  if args.check:
    if args.given_password:
      check = getpass.getpass(prompt="Enter password to check:- ")
      strength = Pass_Checker(check)
      show.add_row(["2.","Strength of Password ",strength])
    else:
      strength = Pass_Checker(password)
      show.add_row(["2.","Strength of Password ",strength])

  print(show)
  
if __name__ == "__main__":
  main()