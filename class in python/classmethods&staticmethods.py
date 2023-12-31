class Employee:

    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang ):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
        # Employee.__init__(self, first, last, pay)

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None ):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'python')
dev_2 = Developer('Test', 'Employee', 80000, 'java')

mngr_1 = Manager('rohit', 'singh',90000, [dev_1])

# print(issubclass(Manager, Developer))



# print(mngr_1.email)
#
# mngr_1.add_emp(dev_2)
# mngr_1.remove_emp(dev_1)
#
# mngr_1.print_emps()
# # print(dev_1.email)
# # print(dev_1.prog_lang)
#
#
# # print(dev_1.pay)
# # dev_1.apply_raise()
# # print(dev_1.pay)




