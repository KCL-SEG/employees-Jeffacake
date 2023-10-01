"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salaryRate=None, hourlyRate=None, hours=None, bonusCommission=None, contractCommissionNum=None, contractCommissionRate=None):
        self.name = name
        self.salaryRate = salaryRate
        self.hourlyRate = hourlyRate
        self.hours = hours
        self.bonusCommission = bonusCommission
        self.contractCommissionNum = contractCommissionNum
        self.contractCommissionRate = contractCommissionRate

    def get_pay(self):
        pay = 0
        if self.salaryRate:
            pay+= self.salaryRate
        if self.hourlyRate and self.hours:
            pay += self.hourlyRate * self.hours
        if self.contractCommissionNum and self.contractCommissionRate:
            pay += self.contractCommissionNum * self.contractCommissionRate
        if self.bonusCommission:
            pay+= self.bonusCommission
        return pay

    def __str__(self):
        string = f'{self.name} works on'
        components = []

        if self.salaryRate:
            components.append(f'a monthly salary of {self.salaryRate}')
        if self.hourlyRate:
            components.append(f'a contract of {self.hours} hours at {self.hourlyRate}/hour')
        if self.contractCommissionNum and self.contractCommissionRate:
            components.append(f'commission for {self.contractCommissionNum} contract(s) at {self.contractCommissionRate}/contract')
        if self.bonusCommission:
            components.append(f'a bonus commission of {self.bonusCommission}')

        if components:
            string += ' ' + ' and '.join(components)
        string += f'. Their total pay is {self.get_pay()}.'

        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salaryRate=4000)
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hourlyRate=25, hours=100)
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salaryRate=3000, contractCommissionRate=200, contractCommissionNum=4)
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = Employee('Jan', hours=150, hourlyRate=25, contractCommissionNum=3, contractCommissionRate=220)
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salaryRate=2000, bonusCommission=1500)
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, hourlyRate=30, bonusCommission=600)
print(str(ariel))