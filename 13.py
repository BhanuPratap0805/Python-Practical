# Custom Exception Class
class InvalidNameError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Function to validate name
def validate_name(name):
    if not name.isalpha():  # Checks if all characters are alphabets
        raise InvalidNameError("Name must contain only alphabets (no digits or special characters).")
    return True

# Main Program
try:
    name = input("Enter your name: ")
    if validate_name(name):
        print(f"Hello, {name}!")
except InvalidNameError as e:
    print("Invalid Name Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
