# class Employee:
#     def __init__(self, name1, id1):
#         self.id = id1
#         self.name = name1
#     def display(self):
#         print(self.id, self.name)
#
#
# emp1 = Employee("Radhika", 101)
# emp1.name="ammu"
# del emp1.id
# emp1.display()
# emp2= Employee("abcd",33)
# emp2.display()

class Student:
    def __init__(self,name,address):
        self.name1=name
        self.address1=address
    def open(self):
        print("hi",self.name1,"school open")

obj=Student("abcd","address")
obj.open()
obj.name1="ammu"
obj.open()
obj1=Student("achu",'kozhikode')
print(obj1.name1)
print(obj1.address1)
