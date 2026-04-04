#expense tracker program: where the expense is added like {amount} and {category} 

expenses = []

while True:
  print("1. Add an expense\n2. View all expenses\n3. Show total spending\n4. Exit")
  choice = input("Enter your choice: ")
  if choice == '1':
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append({"amount":amount,"category":category})
  elif choice == '2':
    if not expenses:
      print("No expenses to view")
    else:
      for i,e in enumerate(expenses,start=1):
        print(i,e["amount"],e["category"])
  elif choice == '3':
    total = 0
    for e in expenses:
      total += e["amount"]
    print("Total is", total)
  elif choice == '4':
    print("exiting and exited")
    break
  else:
    print("Invalid choice")
