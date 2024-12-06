# Create a class Employee with attributes like name, position, and salary. Use the constructor (__init__()) to initialize the attributes when an object is created. Write a method to display employee details.

class Employee():
    name=""
    position=""
    salary=0
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def display(self):
        print(f"""Name: {self.name}\nPosition: {self.position}\nsalary: {self.salary}""")    
        
e=Employee("John","Developer",90000)
e.display()    