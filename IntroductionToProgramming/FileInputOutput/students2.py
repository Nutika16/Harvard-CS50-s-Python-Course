
# In this, we used the reader to read the csv file.

import csv

students = []
with open("students2.csv") as file:
     reader = csv.reader(file)
     for name,home in reader:
          students.append({"name":name , "home":home})

for student in sorted(students, key=lambda student: student["name"]):
     print(f"{student['name']} is from {student['home']}")