---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Number Classification ⭐
# Input a number and display whether it is:

# Positive even
# Positive odd
# Negative even
# Negative odd
# Zero
----------------------------------------------------------------------------------------------------------------------------------------------------------------
num = int(input("Enter a number: "))
if num > 0 and num%2==0:
    print("Positive even")
elif num > 0 and num % 2 != 0:
    print("Positive odd")
elif num < 0 and num % 2 == 0:
    print("Negative even")
elif num < 0 and num % 2 != 0:
    print("Negative odd")
elif num == 0:
    print("Zero")
else:
    print("invalid value")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Output 1:
Enter a number: 4
Positive even
Output 2:
Enter a number: 5
Positive odd
Output 3:
Enter a number: -3
Negative odd
Output 4:
Enter a number: -6
Negative even
Output 5:
Enter a number: 0
Zero
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
