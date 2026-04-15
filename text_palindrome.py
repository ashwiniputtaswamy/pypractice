# python program to check if a string/text is palindrome, simple way and using slicing concept
def palindrome(text):
    return text == text[::-1]
print(palindrome("apple"))
print(palindrome("racecar"))

# Output: 
# False
# True
