class Computer:
    # def __init__(self):
    #     self.name="dell"
    #     self.price=200000
    #     self.type="lap"
    def __init__(self,a,b,c):
        self.name=a
        self.price=b
        self.type=c
    def open(self):
        print(self.name+"   loading")



# cmp1=Computer()
cmp1=Computer("Dell",200000,"laptop")
# print(cmp1.name)
print(cmp1.name,cmp1.type)
# print(cmp1.open())





