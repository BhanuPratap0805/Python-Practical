# Function to swap first n characters of two strings
def swap_first_n_chars(str1, str2, n):
    # Make sure n is not larger than either string
    if n > len(str1) or n > len(str2):
        print("Error: n is larger than one of the strings.")
        return str1, str2
    
    new_str1 = str2[:n] + str1[n:]
    new_str2 = str1[:n] + str2[n:]
    return new_str1, new_str2

# Main program
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
n = int(input("Enter number of characters to swap: "))

result1, result2 = swap_first_n_chars(str1, str2, n)

print("After swapping:")
print("First string:", result1)
print("Second string:", result2)
