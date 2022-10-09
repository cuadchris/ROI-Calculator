
class ROI():

    property = 0
    rent = 0
    down_payment = 0

    def setPropertyPrice(self):
        self.property = int(input("How much are you paying for the entire property?: "))

    def setRent(self):
        self.rent = int(input("How much are you charging for rent every month?: "))

    def getDownPayment(self):
        self.down_payment = round(self.property * .2)
        return self.down_payment







example = ROI()
# print(example.getPropertyPrice())
example.setPropertyPrice()
print(example.getDownPayment())
