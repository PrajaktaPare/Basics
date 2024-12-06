# Define a class Animal with a method speak(), which prints a generic message like "Animal sound". Then create subclasses Dog and Cat that override the speak() method with their respective sounds.
# Bonus: Demonstrate method overriding by calling speak() on objects of Animal, Dog, and Cat.

class Animal():
    def speak(self):
        print("Animal Sound")
class Dog(Animal):
    def speak(self):
        print("Bark")
class Cat(Animal):
    def speak(self):
        print("Meow")        
c=Cat()
c.speak()
d=Dog()
d.speak()                
        