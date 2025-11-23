# for i in [1,"Apple",16.3]:
#     print(i, end=" ") # if you want to print in one line then use the end otherwise don't

students = ["Hermione" , "Harry" , "Ron"]
# for student in students:
#     print(student)

# Alternative way of doing the above question is 
for i in range(len(students)):
    print(i+1, students[i])