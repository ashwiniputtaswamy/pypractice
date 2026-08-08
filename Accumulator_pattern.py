---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program 1: Bus Passenger Counter 🚌
---------------------------------------------------------------------------------------------------------------------------------------------------------------
total = 0
for i in range(3):
    passenger = int(input(f'enter the number of passengers boarded in stop {i+1}: '))
    total = total + passenger
print(f"total passengers boarded are, {total} ")
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Output:
enter the number of passengers boarded in stop 1: 10
enter the number of passengers boarded in stop 2: 20
enter the number of passengers boarded in stop 3: 30
total passengers boarded are, 60 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program 2: Canteen Sales Counter 🍔
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
n = int(input("Enter the number of customers visited the shop: "))
total = 0
for i in range(n):
    items = int(input(f"Enter the number of items bought by customer {i+1}: "))
    total = total + items
print("The total items sold are, ",total)
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Output:
Enter the number of customers visited the shop: 2
Enter the number of items bought by customer 1: 4
Enter the number of items bought by customer 2: 10
The total items sold are,  14
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
