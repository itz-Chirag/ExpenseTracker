import csv

class ExpenseTracker():
    def __init__(self):
        userName = str(input("Enter You Name : "))
        print("You can perform following tasks -\n1. Add Expenses\n2. Remove Expenses\n3.View Expenses ")
        userWants = int(input("What would you like to do : "))
        if userWants == 1 :
            self.AddExpense(userName)
        # elif userWants == 2:
        #     self.
        elif userWants == 3:
            self.ViewExpenses(userName)

    def AddExpense(self, userName):
        self.category = str(input("Whats the category? : "))
        self.amount = float(input("Amount (only integers and decimals) : "))
        self.date = str(input("Date (DD/MM/YY) : "))
        self.description = str(input("Description (if any) : "))
        self.expense = {'Category': self.category, 'Amount': self.amount,
                        'Date': self.date, 'Description': self.description}
        with open('Expenses for ' + userName + '.csv', 'a', newline = '') as csvfile:
            fieldnames = ['Category', 'Amount', 'Date', 'Description']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = '|')
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(self.expense)
        print("Successfully Added")
        print("You can perform following tasks -\n1. Add Expenses\n2. Remove Expenses\n3.View Expenses")
        print("4. Done")
        userWants = int(input("What would you like to do : "))
        if userWants == 1 :
            self.AddExpense(userName)
        elif userWants == 2:
            self.RemoveExpense(userName)
        elif userWants == 3:
            pass
            # self.ViewExpenses(userName)
        elif userWants == 4:
            pass


    def RemoveExpense(self, userName):
        try:
            with open('Expenses for ' + userName + '.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter='|')
        except FileNotFoundError:
            print("No expenses recorded yet")
            
    def ViewExpenses(self, userName):
        try:
            with open('Expenses for ' + userName + '.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter='|')
                print(f"{'Category':<15} {'Amount':<10} {'Date':<12} {'Description':<30}")
                print("-" * 60)
        
                for row in reader:
                    print(f"{row['Category']:<15} {row['Amount']:<10} {row['Date']:<12} {row['Description']:<30}")
        
        except FileNotFoundError:
            print("No expenses recorded yet.")





p1 = ExpenseTracker()
