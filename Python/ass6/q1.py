# Create a class Car with two attributes: brand and year. Write a method display_info() that prints the car's brand and year. Then, create an object of the Car class and call the display_info() method to display the car's details. Bonus: Add an attribute for color and include it in the display_info() method!

class Car():
    brand=" "
    year=0
    bonus=0
    colour=""
    def __init__(self,brand,year,bonus,colour):
        self.brand=brand
        self.year=year
        self.bonus=bonus
        self.colour=colour
    def display_info(self):
        print(f"Brand : {self.brand} \nYear : {self.year}\nBonus : {self.bonus}\ncolour : {self.colour}")
        
c=Car('TATA',2026,20000,'Black');
c.display_info()        
