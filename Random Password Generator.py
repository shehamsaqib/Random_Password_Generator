import random
import string

def generate_password(length):
    """

    :rtype: object
    """
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(length))
    return password

if __name__ == '__main__':
    password_length = int(input("Enter password length: "))
    password = generate_password(password_length)
    print("Generated password: ", password)
