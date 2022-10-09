
class ROI():

# *** Initial attributes ***

    property = 0
    rent = 0
    down_payment = 0
    TOTAL_INCOME = 0

# *** Expenses ***

    tax = 0                     #0.00075 of property price
    insurance = 0               #0.0005 of property price
    vacancy = 0                 #0.05 of total rent
    repairs = 0                 #0.05 of total rent
    cap_exp = 0                 #0.05 of total rent
    property_manager = 0        #0.1 of total rent
    mortgage = 0
    TOTAL_EXPENSES = 0          # all the above added together

# *** CASH FLOW ***

    CASH_FLOW = 0               # This will be total income - total expenses

# *** TOTAL INVESTMENT ***

    closing_costs = 0           # .015 of property
    rehab = 0                   # .035 of property
    TOTAL_INVESTMENT = 0        # This will be closing costs, rehab, and down payment added together


    def setPropertyPrice(self):
        self.property = int(input("How much are you paying for the entire property?: "))

    def setRent(self):
        self.rent = int(input("How much are you charging for rent every month?: "))

    def getDownPayment(self):
        self.down_payment = round(self.property * .2)
        return self.down_payment

    def getTax(self):
        self.tax = round(.00075 * self.property)
        return self.tax

    def getInsurance(self):
        self.insurance = round(.0005 * self.property)
        return self.insurance

    def getPropertyManager(self):
        self.property_manager = round(.1 * self.rent)
        return self.property_manager

    def setMisc(self):
        self.vacancy = round(self.rent * .05)
        self.repairs = round(self.rent * .05)
        self.cap_exp = round(self.rent * .05)

    def getMortgage(self):
        self.mortgage = round((.05/12)*(1/(1-(1+.05/12)**(-360)))*(self.property - self.getDownPayment() ))
        return self.mortgage

    def getTotalIncome(self):
        self.TOTAL_INCOME = self.rent
        return self.TOTAL_INCOME

    def getTotalExpenses(self):
        self.TOTAL_EXPENSES = self.getTax() + self.getInsurance()+  self.vacancy + self.repairs + self.cap_exp + self.getPropertyManager() + self.getMortgage()
        return self.TOTAL_EXPENSES

    def getCashFLow(self):
        self.CASH_FLOW = self.getTotalIncome() - self.getTotalExpenses()
        return self.CASH_FLOW





example = ROI()
example.setPropertyPrice()
example.setRent()
example.setMisc()
print(example.getCashFLow())
