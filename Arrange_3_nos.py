-------------------------------------------------------------------------------------------------------------------------------------------------------------
Arrange Three Numbers
Input three numbers and display them in descending and ascending order.
--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Output in descending order
num = int(input("Enter a 3-digit number: "))
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10
if digit1 > digit2 and digit1 > digit3 and digit2 > digit3:
    print(digit1,digit2,digit3)
elif digit1 > digit2 and digit1 > digit3 and digit3 > digit2:
    print(digit1,digit3,digit2)
elif digit2 > digit1 and digit2 > digit3 and digit1 > digit3:
    print(digit2, digit1, digit3)
elif digit2 > digit1 and digit2 > digit3 and digit3 > digit1:
    print(digit2, digit3, digit1)
elif digit3 > digit1 and digit3 > digit2 and digit1 > digit2:
    print(digit3, digit1, digit2)
elif digit3 > digit1 and digit3 > digit2 and digit2 > digit2:
    print(digit3, digit2, digit1)
else:
    print(digit1,digit2,digit3)
--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Output in ascending order
num = int(input("Enter a 3-digit number: "))
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10
if digit1 > digit2 and digit1 > digit3 and digit2 > digit3:
    print(digit3,digit2,digit1)
elif digit1 > digit2 and digit1 > digit3 and digit3 > digit2:
    print(digit2,digit3,digit1)
elif digit2 > digit1 and digit2 > digit3 and digit1 > digit3:
    print(digit3, digit1, digit2)
elif digit2 > digit1 and digit2 > digit3 and digit3 > digit1:
    print(digit1, digit3, digit2)
elif digit3 > digit1 and digit3 > digit2 and digit1 > digit2:
    print(digit2, digit1, digit3)
elif digit3 > digit1 and digit3 > digit2 and digit2 > digit2:
    print(digit1, digit2, digit3)
else:
    print(digit1,digit2,digit3)
------------------------------------------------------------------------------------------------------------------------------------------------------------------
