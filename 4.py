# Function to check type of character
def check_character(ch):
    if ch.isalpha():
        print(f"{ch} is a letter.")
        if ch.isupper():
            print("It is an uppercase letter.")
        else:
            print("It is a lowercase letter.")
    elif ch.isdigit():
        print(f"{ch} is a numeric digit.")
        print("Its name is:", digit_to_text(ch))
    else:
        print(f"{ch} is a special character.")

# Function to convert digit to text
def digit_to_text(digit):
    names = {
        '0': "ZERO",
        '1': "ONE",
        '2': "TWO",
        '3': "THREE",
        '4': "FOUR",
        '5': "FIVE",
        '6': "SIX",
        '7': "SEVEN",
        '8': "EIGHT",
        '9': "NINE"
    }
    return names[digit]

# Main program
ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character!")
else:
    check_character(ch)
