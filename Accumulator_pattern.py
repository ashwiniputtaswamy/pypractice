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
