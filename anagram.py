🧠 What is an Anagram?
Two strings are anagrams if:
They contain the same characters
In different order
👉 Example:
"listen" and "silent" ✅
"hello" and "world" ❌
-------------------------------------------------------------------------------------------------
# python program to find whether two strings are anagram or not using sorted function
def is_anagram(s1,s2):
    return sorted(s1) == sorted(s2)
print(is_anagram("silent","listen"))
print(is_anagram("man","nan"))

Output:
True
False
