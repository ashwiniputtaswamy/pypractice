# Python program to calculate area and circumference of a circle using function
def circle_calculations(radius):
    area = 3.14 * (radius**2)
    circumference = 2 * 3.14 * radius
    return area, circumference

x,y=circle_calculations(2)
print(f'Area of circle is {x} and circumference of circle is {y}')

# using math module
def circle_calculations(radius):
    import math
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference

# Interactive with formatting
radius = float(input("Enter radius: "))
area, circ = circle_calculations(radius)

print(f"\n📊 Circle Statistics (r = {radius}):")
print(f"{'─' * 30}")
print(f"📍 Area:         {area:>10.2f} sq units")
print(f"📍 Circumference:{circ:>10.2f} units")
