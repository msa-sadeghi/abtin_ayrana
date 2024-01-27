class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name} is barking")
        
    def eat(self):
        print(f"{self.name} is eating")
        
class Beagle(Dog):
    def __init__(self, name, age, is_gunshy):
        super().__init__(name, age)
        self.is_gunshy = is_gunshy
        
    def hunt(self):
        print(f"{self.name} is hunting")
        

b1 = Beagle("jessi", 11, True)
b1.eat()
b1.hunt()
    
