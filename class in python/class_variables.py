class Employee:  # A class is a blueprint for creating instances and each unique employee
     # we create using our employee class will be an instances of the class.
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +  '.' + last + '@ company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def apply_raise (self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('shivam', 'kumar',50000)
emp_2 = Employee('test', 'user',60000)

print(Employee.num_of_emps)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)



