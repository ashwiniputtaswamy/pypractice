# Finding largest of three numbers using python functions
def large_no(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= c and b >= a:
        return b
    else:
        return c

result=large_no(1,30,30)
print("The largest number is", result)

# Finding largest of 3 numbers using python function and built in max function
def large_no(a,b,c):
    return max(a,b,c)
    
result = large_no(1,5,30)
print("the largest number",result)

# finding both smallest and largest numbers using python functions and min and max built in functions
def large_no(a,b,c):
    return max(a,b,c), min(a,b,c)

x,y,z = large_no(1,5,30)
print(f'Largest = {x}, Smallest = {y}')

# finding smallest, largest and the middle number
def large_no(a,b,c):
    largest=max(a,b,c)
    smallest=min(a,b,c)
    middle=(a+b+c)-(smallest+largest)
    return largest, smallest, middle

x,y,z=large_no(345,543,30)
print(f'Largest = {x}, Smallest = {y}, middle = {z}')
