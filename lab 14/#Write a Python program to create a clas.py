#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius

# Example usage
r = float(input("Enter radius of the circle: "))
c = Circle(r)

print(f"Area of the circle: {c.area():.2f}")
print(f"Perimeter of the circle: {c.perimeter():.2f}")
