import random
import string

def generate_password(length=10):
    # Combining letters (uppercase + lowercase) and digits
    characters = string.ascii_letters + string.digits
    # Randomly choosing 'length' number of characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(f"Generated Password: {generate_password(8)}")