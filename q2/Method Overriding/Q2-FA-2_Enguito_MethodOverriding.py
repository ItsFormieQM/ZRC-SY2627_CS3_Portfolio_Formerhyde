class Patient:
    def __init__(self,name,bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    def get_name(self):
        print(f"Name: {self.__name}")
        return self.__name
    def set_name(self,name):
        self.__name = name
        print("Name set to {self.__name}")
    def get_bill_amount(self):
        print(f"Bill Amount: PHP {self.__bill_amount}")
        return self.__bill_amount
    def set_bill_amount(self,bill_amount):
        self.__bill_amount = bill_amount
        print(f"Bill amount set to ${self.__bill_amount}")
    def calculate_bill(self):
        print(f"Final Bill: PHP {self.__bill_amount}")
class Senior_Patient(Patient):
    def __init__(self,name,bill_amount):
        super().__init__(name,bill_amount)
    def calculate_bill(self):
        other_bill = super().get_bill_amount()
        print(f"Final Bill: PHP {other_bill - (other_bill * 0.2)}")
class PhilHealth_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        other_bill = super().get_bill_amount()
        print(f"Final Bill: PHP {other_bill - (other_bill * 0.15)}")
print("---Hospital Billing System---\n")
p1 = Patient("Formerhyde",15000.00)
p1.get_name()
p1.get_bill_amount()
p1.calculate_bill()
print()
p2 = Senior_Patient("Maria Santos",15000.0)
p2.get_name()
p2.calculate_bill()
print()
p3 = PhilHealth_Patient("Pedro Reyes",15000.0)
p3.get_name()
p3.calculate_bill()