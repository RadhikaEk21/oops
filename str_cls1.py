class Subject:
    def __init__(self,name,time):
        self.english=name
        self.maths=time

    def sum(self):
        print(self.english+"  class started")


Sub1=Subject("maths",330)
Sub2=Subject("english",990)
c=(Sub2.english)
print(c)