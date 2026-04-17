# Python program to create_profile(name, age, city="Unknown", country="USA") that returns a dictionary with profile info
def create_profile(name,age,city="Unknown",country="USA"):
    profile = {
        "name":name,
        "age":age,
        "city":city,
        "country":country
    }
    return profile

profile1 = create_profile("Sam",25)
profile2 = create_profile("Ram",25,"Delhi","India")
print(profile1)
print(profile2)

# Output:
# {'name': 'Sam', 'age': 25, 'city': 'Unknown', 'country': 'USA'}
# {'name': 'Ram', 'age': 25, 'city': 'Delhi', 'country': 'India'}

# The pretty print version of the above program
def create_profile(name, age, city="Unknown", country="USA"):
    profile = {
        "name": name,
        "age": age,
        "city": city,
        "country": country
    }
    return profile

def display_profile(profile):
    """Nicely format and display the profile"""
    print("\n" + "="*40)
    print(f"📋 PROFILE: {profile['name']}")
    print("="*40)
    print(f"🎂 Age:     {profile['age']}")
    print(f"🌆 City:    {profile['city']}")
    print(f"🌍 Country: {profile['country']}")
    print("="*40)

# Create and display profiles
p1 = create_profile("Alice Wonder", 28, "Paris", "France")
p2 = create_profile("Bob Builder", 35)  # Uses defaults
p3 = create_profile("Charlie Brown", 9, city="Denver")

display_profile(p1)
display_profile(p2)
display_profile(p3)

#output:

# ========================================
# 📋 PROFILE: Alice Wonder
# ========================================
# 🎂 Age:     28
# 🌆 City:    Paris
# 🌍 Country: France
# ========================================

# ========================================
# 📋 PROFILE: Bob Builder
# ========================================
# 🎂 Age:     35
# 🌆 City:    Unknown
# 🌍 Country: USA
# ========================================

# ========================================
# 📋 PROFILE: Charlie Brown
# ========================================
# 🎂 Age:     9
# 🌆 City:    Denver
# 🌍 Country: USA
# ========================================
---------------------------------------------------------------------------------------------------------------------------------
# python program to calculate sum of even numbers in a list of numbers(without using a function)
a=[1,2,3,4,5,6,7,8]
even_total=0
for i in a:
    if i%2==0:
        even_total += i
print(even_total)
-----------------------------------------------------------------------------------------------------------------------
# python program to calculate sum of even numbers in a list of numbers(with using a function)
def even_sum(numbers):
    total = 0
    for i in numbers:
        if i%2==0:
            total += i
    return total

print(even_sum([1,2,3,4,5,6,7,8]))
----------------------------------------------------------------------------------------------------------------------------

# python program to find both sum of even and odd numbers in a list of numbers using function
def even_odd_sum(numbers):
    even_total = 0
    odd_total = 0
    for i in numbers:
        if i % 2 == 0:
            even_total += i
        else:
            odd_total += i
    return even_total, odd_total
    
x,y = even_odd_sum([1,2,3,4])
print(f"Even = {x}, Odd = {y}")
--------------------------------------------------------------------------------------------------------------------------

# python program to count frequency of characters using dictionary
text = "banana"
count = {}
for char in text:
    count[char]=count.get(char,0)
print(count)

Output: {'b': 1, 'a': 3, 'n': 2}
---------------------------------------------------------------------------------------------------------------------------
# python program to count frequency of characters using dictionary and printing in sorted form
text = "banana"
count = {}
for char in text:
    count[char]=count.get(char,0)+1
for key,value in sorted(count.items()):
    print(f"{key} -> {value}")

Output:
a -> 3
b -> 1
n -> 2

