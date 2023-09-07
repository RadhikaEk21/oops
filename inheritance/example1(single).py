class School:
    def open(self):
        print("School open")  
class Class1(School):
    def started(self):
        print("Class started")
d = Class1()
d.open()
d.started()

