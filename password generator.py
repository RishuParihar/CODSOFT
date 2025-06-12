import string
import random

def generate_password(length):
    # Define characters: letters (uppercase & lowercase), digits, symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # Use random.choices for secure and fast selection
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter desired password length (e.g., 12): "))
            if length < 4:
                print("Password should be at least 4 characters long.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
