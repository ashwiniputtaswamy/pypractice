# shopping cart program using list

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print()
print(f"the total is ${total}")

Output:
Enter a food to buy (q to quit): pizza
Enter the price of a pizza: $1.99
Enter a food to buy (q to quit): steak
Enter the price of a steak: $5.00
Enter a food to buy (q to quit): q
-----YOUR CART-----
pizza steak
the total is $6.99
