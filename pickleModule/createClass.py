class Animal:
    def __init__(self, name, age):
    self.name = name
    self.age = age

    def get_age(self):
        return f"{self.name} is {self.age} years old."
#Creating class for Dog
class Dog(Animal):

    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
    

#Defining a class for cat:
class Cat(Animal):

    # Class attribute (shared by all instances)
    species = "Cat Species"
    
    # Instance method
    def Meow(self):
        return f"{self.name} says woof!"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)  #Accessing attributes and methods

cat1 = Cat("CatName1", 3)
cat2 = Cat("CatName2", 5)

print(dog1.bark())         # Buddy says woof!
print(dog2.get_age())      # Charlie is 5 years old.
print(dog1.species)        # Canis familiaris
# define special methods in classes in python with example(like init, repr, str, getter and setter) also define static method and class method 
#Assignment- s