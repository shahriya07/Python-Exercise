import math
print("Program to calculate the area and circumference of a circle")
radius = float( input("Enter the value of radius: "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
print("Area = ", round(area, 2))
print("Circumference = ", round(circumference, 2))
