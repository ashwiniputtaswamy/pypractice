# shopping cart program using dictionary

cart = {}
total = 0

while True:
    # print("------WELCOME TO YOUR CART-------")
    food = input('Enter the food to buy (press q to exit): ')
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'Enter the price of the {food}: \u20B9'))
        cart[food]=price

print('-----YOUR CART-----')
for key, value in cart.items():
    print(f'{key} --> \u20B9{value}')

for price in cart.values():
    total += price
print(f'The total is \u20B9{total}')
