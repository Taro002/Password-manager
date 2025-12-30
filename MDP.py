import random
import string

print("Password generator")

length = int(input("Enter password length: "))

lower = input("Lowercase letters? (y/n): ")
upper = input("Uppercase letters? (y/n): ")
numbers = input("Numbers? (y/n): ")
symbols = input("Symbols? (y/n): ")

characters = ""
password = ""

# Add characters depending on user choice
if lower == "y":
    characters = characters + string.ascii_lowercase

if upper == "y":
    characters = characters + string.ascii_uppercase

if numbers == "y":
    characters = characters + string.digits

if symbols == "y":
    characters = characters + string.punctuation

# Check if at least one option is selected
if characters == "":
    print("You must choose at least one option")
else:
    for i in range(length):
        password = password + random.choice(characters)

    print("Your password is:", password)
