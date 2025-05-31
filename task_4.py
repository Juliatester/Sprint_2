class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls, name, rest_days, email=None):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f'{name}@email.com'
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment
    
    def salary(self):
        return self.hours * self.hourly_payment


emp1 = EmployeeSalary('Иван', hours=40, rest_days=2, email='ivan@company.com')
print(f'{emp1.name}: {emp1.salary()} руб.')


emp2 = EmployeeSalary.get_hours('Мария', rest_days=1, email='maria@company.com')
print(f'{emp2.name}: {emp2.salary()} руб.')

emp3 = EmployeeSalary.get_email('Алексей', hours=35, rest_days=2)
print(f'{emp3.email}: {emp3.salary()} руб.')

EmployeeSalary.set_hourly_payment(450)
print(f'Новая зарплата Марии: {emp2.salary()} руб.')