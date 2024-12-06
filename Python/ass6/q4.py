# Create a class Vehicle with attributes brand and speed. Add a method show_details() to display these details. Then, create a subclass Car that inherits from Vehicle and adds an attribute mileage. Use the super() method to call the show_details() of the parent class inside the Car class's show_details() method.

class Vehicle ():
    brand=""
    speed=0
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def show_details(self):
        print(f"Brand : {self.brand}\nSpeed : {self.speed}")

class Car(Vehicle):
    mileage=0
    def __init__(self,brand,speed,mileage):
        super().__init__(brand,speed)
        self.mileage=mileage
    def show_details(self):
        super().show_details()
        print(f"Mileage: {self.mileage}")            
        
c=Car("TATA",90,70)        
c.show_details()