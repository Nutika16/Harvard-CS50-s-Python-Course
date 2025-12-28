# def meow(n: int):
#     for _ in range(n):
#         print(meow)

# # number: int = input("Number: ") # this will throw an error and mypy will help you recognize it quickly
# number: int = int(input("Number: "))
# meow(number)


def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows,end= "")