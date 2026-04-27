----------------------------------------------------------------------------------------------------------------------------------------------------
# Python scenario based interview questions
----------------------------------------------------------------------------------------------------------------------------------------------------
# Question 1: Input String: text = "Analytics2026". Extract only the digits from the string (remove letters and other characters)
# Expected Output: 2026

text = "Analytics2026"

digits_only = ''.join([char for char in text if char.isdigit()])
print(digits_only)

# Output: 2026
-----------------------------------------------------------------------------------------------------------------------------------------------------
# Question 2: Input list: numbers = [1,5,2,8,3,7]. Use list comprehension to create a new list with squares of even numbers only.
# Expected Output: [4, 64]

numbers = [1,5,2,8,3,7]

sq_even_no = [x ** 2 for x in numbers if x % 2 == 0]
print(sq_even_no)

# Output: [4, 64]
-----------------------------------------------------------------------------------------------------------------------------------------------------
# Question 3: Input list: data = [10,25,5,30,15,20]. Use list comprehension to create a new list with only numbers greater than 15 multiplied by 2.
# Expected Output: [50,60,40]

data = [10,25,5,30,15,20]

filtered_doubled = [x * 2 for x in data if x > 15]
print(filtered_doubled)

# Output: [50, 60, 40]
------------------------------------------------------------------------------------------------------------------------------------------------------
