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
# output: Largest = 543, Smallest = 30, middle = 345

# finding smallest, largest and the middle number using sort function
def large_no(a,b,c):
    nums=sorted([a,b,c])
    return nums[2], nums[0], nums[1]

x,y,z=large_no(1,5,30)
print(f'Largest = {x}, Smallest = {y}, middle = {z}')

# python program to find smallest, largest and middle number using sorted function for 5 numbers
def large_no(a,b,c,d,e):
    nums=sorted([a,b,c,d,e])
    return nums[4],nums[0],nums[2]
x,y,z=large_no(1,9,3,7,5)
print(f'Largest = {x}, Smallest = {y}, Middle = {z}')


# python program to find second largest number in the list without using sorted function
def sec_large(numbers):
    largest = float('-inf')
    second = float('-inf')
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second
print(sec_large([1,5,3,9,7]))
