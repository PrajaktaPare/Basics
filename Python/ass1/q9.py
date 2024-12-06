weight=float(input("Enter weight (in kg) : "))
height=float(input("Enter height (in m) : "))
BMI=weight/(height**2)
print(f"BMI is {BMI:.2f}")
if BMI<14.5:
    print("Underweight!")
elif 14.5<BMI<23.9:
    print("Normal!")
else:
    print("Overweight!")
            