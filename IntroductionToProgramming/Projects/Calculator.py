num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

str = input("ENTER THE EXPRESSION: ")

# Addition
if(str == "+"):
    print(num1 + num2)
elif(str == '-'):
    print(num1 - num2)
elif(str == '*'):
    print(num1 * num2)
elif(str == "/"):
    print(num1 / num2)
elif(str == "%"):
    print(num1 % num2)
else:
    print("Not a valid expression")
