# employee salary calculation using constructors


class Employee:
    def __init__(self, name, basic_salary, bonus, deductions):
        self.name = name
        self.basic_salary = basic_salary
        self.bonus = bonus
        self.deductions = deductions

    def calculate_salary(self):
        total_salary = self.basic_salary + self.bonus - self.deductions
        return total_salary
employee1 = Employee("John Doe", 50000.0, 2000.0, 1500.0)
total_salary = employee1.calculate_salary()
print(f"Employee: {employee1.name}")
print(f"Total Salary: {total_salary}")