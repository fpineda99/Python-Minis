import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars= string.punctuation
    
    characters = letters + digits + special_chars
    
    password = ""
    
    for _ in range(length):
        password += random.choice(characters)
        
    return password
    
def main():
    password_length = int(input("Enter your password length: "))
    password = generate_password(password_length)
    print("Generated password: ", password)
    
if __name__ == "__main__":
    main()