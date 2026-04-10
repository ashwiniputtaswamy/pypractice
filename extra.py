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
