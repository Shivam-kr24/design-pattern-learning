# Python Object-Oriented Programming
#    1. Classes and Instances.....


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('shivam', 'kumar', 50000)
emp_2 = Employee('test', 'user', 60000)

# print(emp_1)
# print(emp_2)


# print(emp_1.email)
# print(emp_2.email)
#
# # print('{} {}'.format(emp_1.first, emp_1.last))
# print(emp_1.fullname())
# print(emp_2.fullname())
emp_1.fullname()
print(Employee.fullname(emp_1))