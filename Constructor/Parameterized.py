class Employee:
    def __init__(self, name1, id1):
        self.id = id1
        self.name = name1
    def display(self):
        print(self.id, self.name)


emp1 = Employee("Radhika", 101)
emp1.name="ammu"
del emp1.id
emp1.display()
emp2= Employee("abcd",33)
emp2.display()

