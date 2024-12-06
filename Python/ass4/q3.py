employee_data = ('John', 'Doe', 34, 'Developer', 'New York')
fname,lname,age,jobtitle,city=employee_data
print(f"First name : {fname}")
print(f"Last name : {lname}")
print(f"Age : {age}")
print(f"Job Title : {jobtitle}")
print(f"City : {city}")

if 'Developer' in employee_data:
    print("Developer is present")
    
    
emp_list=list(employee_data)
emp_list.append('Full-Time') 
print(emp_list)   