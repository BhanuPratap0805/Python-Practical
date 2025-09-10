# Function to get cubes of even integers using a for loop
def cubes_even_for_loop(input_list):
    result = []
    for item in input_list:
        if isinstance(item, int) and item % 2 == 0:
            result.append(item ** 3)
    return result

# Function to get cubes of even integers using list comprehension
def cubes_even_list_comprehension(input_list):
    return [item ** 3 for item in input_list if isinstance(item, int) and item % 2 == 0]

# Main program
# Sample list (can have integers, strings, floats, etc.)
input_list = [1, 2, "hello", 3.5, 4, 6, "world", 7, 8]

print("Input List:", input_list)

# a. Using for loop
print("Cubes of even integers (for loop):", cubes_even_for_loop(input_list))

# b. Using list comprehension
print("Cubes of even integers (list comprehension):", cubes_even_list_comprehension(input_list))
