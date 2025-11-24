#Approach 1:
try:
    x = int(input("What's X?? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# Approach 2: Use try / except / else (clean)
try:
    x = int(input("What's X?? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# Approach 3: Keep asking until a valid integer is entered (robust user input)
while True:
    try:
        x = int(input("What's X?? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")

# Approach 4: By creating functions
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x 
        except ValueError:
            print("Given value of X is not an integer") #We can also use pass here it means you are still catching 
                                                        #the value but passing it. It will not show anything to user. 

def main():
    x = get_int("What's X? ")
    print(f"Value of x is {x}")

main()