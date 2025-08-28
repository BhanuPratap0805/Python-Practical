import cmath  # To handle complex numbers

def find_roots(a, b, c):
    if a == 0:
        print("This is not a quadratic equation.")
        return

    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the two roots
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)

    print(f"The roots of the equation {a}x² + {b}x + {c} = 0 are:")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")

# Example usage:
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

find_roots(a, b, c)
