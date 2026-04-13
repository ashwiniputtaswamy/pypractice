# python program to count the vowels in the string using functions
def vowel_count():
    text = input("enter string: ")
    count = 0
    vowels = 'aeiouAEIOU'
    
    for char in text:
        if char in vowels:
            count += 1
    return count    
            
print(vowel_count())

