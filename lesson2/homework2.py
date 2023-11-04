class Cat:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printer(self):
        print("Name of cat",self.name)
        print("Age of cat", self.age)

first_cat = Cat("Alen",3)
first_cat.printer()