import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method to display the point in (x, y) format
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Method to calculate distance between two points
    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


# Main program
print("Enter coordinates for Point 1:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("\nEnter coordinates for Point 2:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# Create Point objects
p1 = Point(x1, y1)
p2 = Point(x2, y2)

# Print points
print("\nPoint 1:", p1)
print("Point 2:", p2)

# Calculate distance
print(f"\nDistance between {p1} and {p2} is: {p1.distance(p2):.2f}")
