# In this we are going to format the unformatted data provided by the user according to our requirement 
import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$",name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")