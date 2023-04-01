# 9.1 Write a Python class named Circle constructed by a radius and two methods which will
# compute the area and the perimeter of a circle.

class Circle:
    def areaOfCircle(self, radius):
        return (3.14 * radius * radius)

    def perimeterOfCircle(self, radius):
        return (2*3.14 *radius)

print("Program to find area and perimeter of a circle:\n")
radius = int(input("Enter the value of radius of any circle: "))
result1 = Circle.areaOfCircle(0, radius)
result2 = Circle.perimeterOfCircle(0, radius)

print(f"Area: {result1}.\nPerimeter: {result2}")
print("\nID No: 21DCE042\nAuthor: Karangiya Jash Ramde")

