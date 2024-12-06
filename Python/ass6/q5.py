# Define two classes, Engine and Body, with constructors that initialize respective attributes like horsepower and material. Then, create a class Car that inherits from both Engine and Body. Use the super() method to initialize both parent class attributes from the Car class. 

class Engine():
    horsepower=0
    def __init__(self,horsepower):
        self.horsepower=horsepower
    def displayE(self):
        print(f"Horsepower: {self.horsepower}") 
        
class Body():
    material=""
    def __init__(self,material):
        self.material=material
    def displayB(self):
        print(f"Material: {self.material}") 
        
class Car(Engine,Body):
    brand=""
    def __init__(self,horsepower,material,brand):
        super().__init__(horsepower)                      
        Body.__init__(self,material)
        self.brand=brand
    def display(self):
        super().displayE() 
        super().displayB()   
        print(f"Brand : {self.brand}")
        
c= Car("TATA","TATA","TATA")
c.display()