# def hello(name):
#     print(f"Hello, {name}")

# name = input("What is your name? ")
# hello(name)


# Function Order & Using `main()`
def main():
    name = input("What is your name?? ")
    hello(name)

def hello(name):
    print(f"Hello, {name}")

main()

# Function using return statement 
def main():
    name = input("What is your name? ")
    return name

def hello(name):
    print("f Hello, {name}")

main()