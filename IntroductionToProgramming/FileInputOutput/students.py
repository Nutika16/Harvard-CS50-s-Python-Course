# Retrieving value of the name and house from students.csv

# with open("students.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         # or
#         name , house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

# Retrieving value as well as sorting it...Using the below approach you can sort on the basis of name or house 
students = []
with open("students.csv") as file:
     for line in file:
          name , house = line.rstrip().split(",")
          student = {"name":name , "house":house}
          students.append(student)

for student in sorted(students, key=lambda student: student["name"] , reverse=True):
     print(f"{student['name']} is in {student['house']}")