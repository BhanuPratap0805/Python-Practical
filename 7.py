# Function to find all occurrences of a substring
def find_all_occurrences(main_str, sub_str):
    indices = []
    start = 0
    while True:
        index = main_str.find(sub_str, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1  # move forward to find next occurrence
    return indices if indices else -1

# Main program
main = input("Enter the main string: ")
sub = input("Enter the substring to search: ")

result = find_all_occurrences(main, sub)

if result == -1:
    print(f"'{sub}' not found in '{main}'.")
else:
    print(f"'{sub}' found at indices: {result}")
