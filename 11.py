# Function to create and print dictionary of cubes
def cubes_dict():
    cube_dict = {}
    for i in range(1, 6):
        cube_dict[i] = i ** 3
    print("Dictionary of cubes (1 to 5):", cube_dict)

# Main program
cubes_dict()
