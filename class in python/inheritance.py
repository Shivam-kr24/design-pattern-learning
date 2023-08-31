class Employee:  # A class is a blueprint for creating instances and each unique employee
    # we create using our employee class will be an instances of the class.
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@ company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
       first, last, pay =emp_str.split('-')
       return cls (first, last, pay)

    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('shivam', 'kumar', 50000)
emp_2 = Employee('test', 'user', 60000)

import datetime
my_date = datetime.date(2023,8,23)

print(Employee.is_working(my_date))












# emp_str_1 = 'John-Doe - 70000'
# emp_str_2 = 'Steve -Smith-30000'
# emp_str_3 = 'jane-Doe-90000'
#
# # first,last,pay = emp_str_1.split('-')
# #
# # new_emp_1: Employee = Employee(first, last, pay)
#
#
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)







