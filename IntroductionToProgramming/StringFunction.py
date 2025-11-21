# Ask for the user's name and remove the whitespace and captialize every first letter
name = input("What is the name? ").strip().title()

# Print a greeting
print(f"Hello, {name}!!")

# Split the name into first and last (assuming two parts)
first, last = name.split(" ")

print(f"Hello, {first}!!")
print(f"Hello, {last}!!")
