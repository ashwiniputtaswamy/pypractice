# Python program to calculate area and circumference of a circle using function
def circle_calculations(radius):
    area = 3.14 * (radius**2)
    circumference = 2 * 3.14 * radius
    return area, circumference

x,y=circle_calculations(2)
print(f'Area of circle is {x} and circumference of circle is {y}')
