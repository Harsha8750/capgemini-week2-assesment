#	8. Design a system where a base class `Animal` has a method `speak()`, 
# and subclasses `Dog` and `Cat` override it.	

class Animal:
    def __init__(self):
        pass
    def speak(self):
        print("Various animals make different sounds")

class Dog(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        print("Bark")

class Cat(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        print("Meow")

dg=Dog()
ct=Cat()
dg.speak()
ct.speak()
    
