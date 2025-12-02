
"""
This script reads data from a CSV file using csv.DictReader.

Why use DictReader?
- DictReader maps each row to a dictionary using the column headers.
- It prevents errors that occur when accessing fields by position.
- You can safely reference values like row["name"] or row["home"] without
  worrying about their order in the file.

The script:
1. Loads all rows into a list of dictionaries.
2. Sorts the list alphabetically by the 'name' field.
3. Prints each person's name along with their home.
""" 

import csv

dict_reader_data = []

with open("DictReaderUsed.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        dict_reader_data.append({"name": row["name"], "home": row["home"], "house":row['house']})

for entry in sorted(dict_reader_data, key=lambda x: x["name"]):
    print(f"{entry['name']} is from {entry['home']} having house {entry['house']}")
