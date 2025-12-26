students = [
    {"name" : "Hermoine" , "house":"Gryffindor"},
    {"name" : "Harry" , "house":"Gryffindor"},
    {"name" : "Ron" , "house":"Gryffindor"},
    {"name" : "Draco" , "house":"Slytherin"},
    {"name" : "Padma" , "house":"Ravenclaw"},
]

# houses = []
houses = set()
for student in students:
    houses.add(student["house"])
    # if student["house"] not in houses:
        # houses.append(student["house"])

for house in sorted(houses):
    print(house)