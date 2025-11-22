def main():
    num = int(input("Enter the number: "))
    print("The square of the given num is:" , square(num))

# def square(num):
#     return num * num

# Another way of doing square is using the pow function
def square(num):
    return pow(num,2)

main()
