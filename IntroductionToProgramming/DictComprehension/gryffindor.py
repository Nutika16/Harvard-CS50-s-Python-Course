students = ["Hermione","Harry","Ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house":"Gryffindor"})

# using dictionary comprehension for doing the same thing i.e. doing by append
gryffindors = [{"name":student,"house":"Gryffindor"} for student in students] # this will print all the dictonaries

# if you want to print just the key and value with the assumption that name is unique 
gryffindors = {student:"Gryffindor" for student in students}


print(gryffindors)

