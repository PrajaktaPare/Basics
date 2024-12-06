student_grades = {'Ram': 85, 'Sham': 92, 'Ojas’': 88, 'Anay': 79}
highest_grade=max(student_grades,key=student_grades.get)
print(f"Highest grade is {highest_grade}")

student_grades['Eve']=95

for stu in sorted(student_grades):
    print(f"{stu}:{student_grades[stu]}")