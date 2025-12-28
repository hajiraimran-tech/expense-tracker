# Mini Project – Expense Tracker

expenses = []  # List of all expenses in form of dictionary
print ("Welcome to Expense Tracker")

while True:
    print ("====MENU====")
    print ("1. Add Expense")
    print ("2. View all Expenses")
    print ("3. View total Expense")
    print ("4. Exit")

    choice = int(input("Please Enter your Choice : "))
# 1. Add Expense
    if (choice == 1):
        print ("====Let's add all your expenses====")
        date = input("Enter date: ")
        category = input("Enter category (Food, Travel, Makeup, Grocery): ")
        description = input("Enter short description: ")
        amount = float(input("Enter amount spent: "))

        expense = {
            "Date" : date,
            "Category" : category,
            "Description" : description,
            "Amount" : amount
        }
        expenses.append(expense)
        print ("\nExpense Added Successfully!")

# 2. View all Expenses
    elif (choice == 2):
        if (len(expenses)==0):
            print ("No Expenses Added.")
        else:
            print ("====Following is all your expense====")
            count = 1
            for eachExpense in expenses:
                print (f"Expense # {count}: Date: {eachExpense["Date"]}, Category: {eachExpense["Category"]}, Description: {eachExpense["Description"]}, Amount: {eachExpense["Amount"]}")
                count += 1

# 3. View total Expense
    elif (choice == 3):
        total = 0
        for eachExpense in expenses:
            total = total + eachExpense["Amount"]         
        print ("\nTotal Expense is : ", total)

# 4. Exit
    elif (choice == 4):
        print ("Thank You for using Expense Tracker")
        break

    else:
        print ("Invalid Choice! Try again.")