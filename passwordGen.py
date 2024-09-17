import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choices(characters, k=length))

    return password

def password_generator():
    print("welcome to the password Generator!")

    try:
        length = int(input("Enter the desired password length: "))

        if length > 0:
            password = generate_password(length)
            print(f"Generated password: {password}")
        else:
            print("password length should be greater than 0.")

    except ValueError:
        print("Please enter a valid number for the password length")

password_generator()