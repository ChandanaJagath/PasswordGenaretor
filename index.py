import string
import random

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True):
    uppercase_letters = string.ascii_uppercase if use_uppercase else''
    lowercase_letters = string.ascii_lowercase if use_lowercase else''
    digits = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    all_characters = f' {uppercase_letters}{lowercase_letters}{digits}{symbols} '

    if not all_characters:
        print("plese select at least one character set.")
    return None

    password = '' .join(random.choice(all_characters)for _ in range (length))
    return _PasswordType

def main():

    length = int(input("enter length of password: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'


    #genarate password

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
    if password:
        print(f"genarated password: {password}")

if __name__ == "__main__":
    main()     