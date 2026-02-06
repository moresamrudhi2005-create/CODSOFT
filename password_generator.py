import random
import string
print("--------PASSWORD GENERATOR--------")
length = int(input ("Enter the desired password length:"))

use_uppercase=input("Include uppercase letter?(yes/no): ").lower()
use_digits= input("Includes Digits ?(yes/no): ").lower()
use_special=input("Includes special symbol? (yes/no): ").lower()
first_capital=input("Includes first letter is capital?(yes/no): ").lower()

characters = string.ascii_lowercase

if use_uppercase == 'yes':
    characters += string.ascii_uppercase

if use_digits == 'yes':
    characters += string.digits

if use_special == 'yes':
    characters += string.punctuation


if length <= 0:
    print("Invalid password length!")
else:
    password=""

    if first_capital=='yes':
        password +=random.choice(string.ascii_uppercase)
        length -=1

        password+= ''.join(random.choice(characters)for _ in range(length))

        print("Generated password:",password)

