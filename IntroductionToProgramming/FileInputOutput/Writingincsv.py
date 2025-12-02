import csv 

name = input("What is your name? ")
home = input("Whar is your home? ")

with open("written.csv", "a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"name":name , "home":home})