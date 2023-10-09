

class Property():
    
    def __init__(self, income = 0, expenses = 0, cash_flow = 0, investment = 0):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.investment = investment
        
        
    def income_user(self):
        rental_income = int(input("How much is the monthly property's rental income? $" ))
        rental_income_duplex = input("Is the rental property a duplex? yes or no > ").lower()
        if rental_income_duplex == 'yes':
            rental_income *= 2
        if rental_income_duplex == 'no':
            rental_income = rental_income
        other_income_sum = []
        other_income = input("Does the property have another source of income, for example a coin based laundry system, storage space to rent out or other miscellaneous income? yes or no > ").lower()
        if other_income == 'no':
            other_income = 0
        elif other_income == 'yes':
            laundry = int(input("Please enter the amount of monthly income average from laundry, or enter '0' if it does not apply. $"))
            other_income_sum.append(laundry)
            storage = int(input("Please enter the amount of monthly income average from storage space rental, or enter '0' if it does not apply. $"))
            other_income_sum.append(storage)
            miscellaneous = int(input("Please enter the amount of any other form of monthly income from rental property, or enter '0' if it does not apply. $"))
            other_income_sum.append(miscellaneous)

            other_income = sum(other_income_sum)
            
        self.income = (rental_income + other_income)
        print(f'\n\tTotal monthly income ${self.income:.0f}\n')
    
    
    def expenses_user(self):
        exp = []
        mortage = int(input('Enter the amount of monthly mortage payments: '))
        exp.append(mortage)
        prop_tax = int(input('Enter the amount of annual property tax (per month): '))
        exp.append(prop_tax)
        insurance = int(input("Enter the amount of monthly home insurance payments: "))
        exp.append(insurance)
        electric = int(input("Enter the average amount of monthly electric bill, or enter '0' if it does not apply:: "))
        exp.append(electric)
        water = int(input("Enter the average amount of monthly water bill, or enter '0' if it does not apply:: "))
        exp.append(water)
        gas = int(input("Enter the average amount of monthly gas bill, or enter '0' if it does not apply:: "))
        exp.append(gas)
        trash = int(input("Enter the amount of monthly trash collection fee, or enter '0' if it does not apply:: "))
        exp.append(trash)
        sewer = int(input("Enter the amount of monthly sewer fee, or enter '0' if it does not apply:: "))
        exp.append(sewer)
        hoa = int(input("Enter the amount of monthly home owners association fee, or enter '0' if it does not apply:: "))
        exp.append(hoa)
        lawn = int(input("Enter the amount of monthly lawn maintenance costs if it applies, otherwise enter '0': "))
        exp.append(lawn)
        snow = int(input("Enter the amount of monthly snow removal costs if it applies, otherwise enter '0': "))
        exp.append(snow)
        repairs = int(input("Enter the amount separated for future repairs if it applies, otherwise enter '0': "))
        exp.append(repairs)
        capex = int(input("Enter the amount separated for big expenses (such as roof replacement) if it applies, otherwise enter '0': "))
        exp.append(capex)
        vacancy = int(input("Enter the amount separated to cover vacancy costs, otherwise enter '0': "))
        exp.append(vacancy)
        prop_management = int(input("Enter property management monthly costs, otherwise enter '0': "))
        exp.append(prop_management)
        
        self.expenses = sum(exp)
        
        print(f"\n\tTotal monthly Expenses ${self.expenses}\n")
        
        
    def cash_flow_user(self):
        self.cash_flow =  self.income - self.expenses
        print(f"\n\tTotal monthly Cash Flow ${self.cash_flow:.0f}\n")
        
        
    def investment_user(self):
        investment_total = []
        down_paymt = int(input("Enter the amount of down payment: "))
        investment_total.append(down_paymt)
        closing = int(input("Enter the amount of closing costs: "))
        investment_total.append(closing)
        rehab_budget = int(input("Enter the amount of rehab budget: "))
        investment_total.append(rehab_budget)
        is_other = input("Is there any other costs or expenses to add? yes or no > ")
        if is_other == 'no':
            other_misc = 0
        else:
            other_misc = int(input("Enter the amount of other costs and expenses: "))
            investment_total.append(other_misc)
        
        self.investment = sum(investment_total)
        print(f"\nTotal investment ${self.investment}\n")
        
        
    def coc_roi_user(self):
        
        self.coc_roi = ((self.cash_flow * 12) / self.investment) * 100
        print(f"\nCash On Cash Return On Investiment = {self.coc_roi:.2f}%\n")