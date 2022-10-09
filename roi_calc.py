import locale
locale.setlocale( locale.LC_ALL, '' )


class ROI():

    # *** Initial attributes ***

    property = 0
    rent = 0
    down_payment = 0
    TOTAL_INCOME = 0

# *** Expenses ***

    tax = 0  # 0.00075 of property price
    insurance = 0  # 0.0005 of property price
    vacancy = 0  # 0.05 of total rent
    repairs = 0  # 0.05 of total rent
    cap_exp = 0  # 0.05 of total rent
    property_manager = 0  # 0.1 of total rent
    mortgage = 0
    TOTAL_EXPENSES = 0          # all the above added together

# *** CASH FLOW ***

    CASH_FLOW = 0               # This will be total income - total expenses

# *** TOTAL INVESTMENT ***

    closing_costs = 0           # .015 of property
    rehab = 0                   # .035 of property
    # This will be closing costs, rehab, and down payment added together
    TOTAL_INVESTMENT = 0

# *** RETURN ON INVESTMENT ***

    roi = 0

    def setPropertyPrice(self):
        self.property = int(
            input("How much are you paying for the entire property?: "))

    def setRent(self):
        self.rent = int(
            input("How much are you charging for rent every month?: "))

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
        self.mortgage = round(
            (.05/12)*(1/(1-(1+.05/12)**(-360)))*(self.property - self.getDownPayment()))
        return self.mortgage

    def getTotalIncome(self):
        self.TOTAL_INCOME = self.rent
        return self.TOTAL_INCOME

    def getTotalExpenses(self):
        self.TOTAL_EXPENSES = self.getTax() + self.getInsurance() + self.vacancy + \
            self.repairs + self.cap_exp + self.getPropertyManager() + self.getMortgage()
        return self.TOTAL_EXPENSES

    def getCashFLow(self):
        self.CASH_FLOW = self.getTotalIncome() - self.getTotalExpenses()
        return self.CASH_FLOW

    def getClosingCosts(self):
        self.closing_costs = round(self.property * .015)
        return self.closing_costs

    def getRehab(self):
        self.rehab = round(self.property * .035)
        return self.rehab

    def getTotalInvestment(self):
        self.TOTAL_INVESTMENT = self.getDownPayment() + self.getClosingCosts() + \
            self.getRehab()
        return self.TOTAL_INVESTMENT

    def getROI(self):
        self.roi = self.getCashFLow() * 12 / self.getTotalInvestment() * 100
        return self.roi

    def summarize(self):
        print("Based on what you've entered, here is a complete summary of your potential investment:")
        print(f'Property price: {locale.currency(self.property, grouping=True).rstrip("0")}')
        print(f'Down payment: {locale.currency(self.getDownPayment(), grouping=True).rstrip("0")} Ideally, this is 20% of the property price.')
        print(f'Rent and total income : {locale.currency(self.rent, grouping=True).rstrip("0")}')
        print(f'Total expenses: {locale.currency(self.getTotalExpenses(), grouping=True).rstrip("0")}\n(This number includes taxes, insurance, a monthly allotment for any future vacancies and repairs, a montly payment for the property manager, and the mortgage)')
        print(f'Cash flow every month after expenses: {locale.currency(self.getCashFLow(), grouping=True).rstrip("0")}')
        print(f'Total investment: {locale.currency(self.getTotalInvestment(), grouping=True).rstrip("0")}\n (This number includes closing costs, down payment, and a modest percentage allocated for any rehab repairs done to the property)')
        print(f'Based on above info, the ROI for this property is an estimated {self.getROI()} percent.')

example = ROI()
example.setPropertyPrice()
example.setRent()
example.setMisc()
example.summarize()
