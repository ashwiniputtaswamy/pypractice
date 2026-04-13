# python program to reverse a string without using a function
text = "apple"
print(text[::-1])


# python program to reverse a string using a function
def rev_string(text):
    return text[::-1]
text = input("enter string/text: ")
print(rev_string(text))
