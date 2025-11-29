'''In this program you have to provide the names everytime you run...Suppose you just want to run the program 
everytime with the same name then it's better to save it somewhere there comes File I/O in picture'''

# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

'''Appending in the file'''

# name = input("What is your Name? ")

# with open("name.txt" , "a") as file:
#     file.write(f"{name}\n")

'''Reading from the file'''
with open("name.txt", "r") as file:
    for line in sorted(file):
        print("hello", line.rstrip())
