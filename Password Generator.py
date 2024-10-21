import random
import string



def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Defining character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''


    all_characters = lowercase + uppercase + numbers + symbols

    if not all_characters:
        raise ValueError("At least one type of character must be selected.")


    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password



try:
    password_length = int(input("Enter the password length: "))

    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'


    password = generate_password(password_length, use_uppercase, use_numbers, use_symbols)
    print(f"Generated Password: {password}")

except ValueError as e:
    print(f"Error: {e}")