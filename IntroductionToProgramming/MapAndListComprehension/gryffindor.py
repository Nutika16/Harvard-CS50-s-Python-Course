students = [
    {"name" : "Hermoine" , "house":"Gryffindor"},
    {"name" : "Harry" , "house":"Gryffindor"},
    {"name" : "Ron" , "house":"Gryffindor"},
    {"name" : "Draco" , "house":"Slytherin"},
    {"name" : "Padma" , "house":"Ravenclaw"},
]

# solved using the list comprehension

# gryffindors = [
#     student["name"] for student in students if student["house"]=="Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

# solved using the filter 
def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor,students)

for gryffindor in sorted(gryffindors, key=lambda s:s["name"]):
    print(gryffindor["name"])