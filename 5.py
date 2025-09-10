# Function to find frequency of a character in a string
def find_frequency(s, ch):
    return s.count(ch)

# Function to replace a character with another
def replace_char(s, old, new):
    return s.replace(old, new)

# Function to remove first occurrence of a character
def remove_first_occurrence(s, ch):
    return s.replace(ch, "", 1)

# Function to remove all occurrences of a character
def remove_all_occurrences(s, ch):
    return s.replace(ch, "")

# Main program
s = input("Enter a string: ")
ch = input("Enter the character to work with: ")

# a. Find frequency
print(f"Frequency of '{ch}' in string: {find_frequency(s, ch)}")

# b. Replace character
new_ch = input("Enter the new character to replace it with: ")
print("After replacing:", replace_char(s, ch, new_ch))

# c. Remove first occurrence
print("After removing first occurrence:", remove_first_occurrence(s, ch))

# d. Remove all occurrences
print("After removing all occurrences:", remove_all_occurrences(s, ch))
