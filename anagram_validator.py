---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Python program to check if two strings are anagrams using sorted()
text1 = input("enter the first text: ")
text2 = input("enter the second text: ")

# convert both the strings to lowercase
text1 = text1.lower()
text2 = text2.lower()

# check is length is same
if len(text1) == len(text2):

    # sort the strings
    sorted_text1 = sorted(text1)
    sorted_text2 = sorted(text2)

    # if sorted char arrays are same
    if sorted_text1 == sorted_text2:
        print(f"{text1} and {text2} are anagram")
    else:
        print(f"{text1} and {text2} are not anagram")

else:
    print(f"{text1} and {text2} are not anagram")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Output:
enter the first text: race
enter the second text: care
race and care are anagram
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
