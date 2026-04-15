# python program to check if a string/text is palindrome, simple way and using slicing concept
def palindrome(text):
    return text == text[::-1]
print(palindrome("apple"))
print(palindrome("racecar"))

# Output: 
# False
# True

# python program to check if a string/text is palindrome, using loop - good practice. Note:output will be boolean as previous or above code
def palindrome(text):
    rev=""
    for char in text:
        rev = char + rev
    return rev == text
print(palindrome("apple"))
print(palindrome("racecar"))
