# def main():
#     student  = get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name , house) # here are returning the tuple

# if __name__ == "__main__":
#     main()

""" we can solve this using dictonary also:"""
# def main():
#     student  = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student["name"]} from {student["house"]}")

# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()

"""What if we have more data for student to be collected then it will be difficult to solve the problem using tuple , dictonary or lists. Hence, we are going to use the classes to solve this"""

class Student:
    def __init__(self, name , house): # add patronus in the signature if you want to print 
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid Error")
        self.name = name
        self.house = house
        # self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🐎"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russel terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"


def main():
    student = get_student()
    student.house = "Number Four, Privet drive" 
    """Here, the problem is anybody can change anything therefore we use property"""
    print(student)
    '''The below statements are used when you want to print patronus'''
    # print("Expecto Patronum")
    # print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # patronus = input("Patronus: ")
    return Student(name , house)
    # return Student(name , house, patronus)

if __name__ == "__main__":
    main()
