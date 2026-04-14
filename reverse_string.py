# python program to reverse a string without using a function
text = "apple"
print(text[::-1])


# python program to reverse a string using a function
def rev_string(text):
    return text[::-1]
text = input("enter string/text: ")
print(rev_string(text))

# python program to reverse a string using a function and for loop and empty string
def rev_string(text):
    rev = ""
    for char in text:
        rev = char + rev
    return rev
print(f'the reverse of the string is "{rev_string("apple")}"')


# Optimized Version (Advanced) of previous one
def rev_string(text):
    rev = []
    for char in text:
        rev.insert(0,char)
    return "".join(rev)
print(rev_string("apple"))
