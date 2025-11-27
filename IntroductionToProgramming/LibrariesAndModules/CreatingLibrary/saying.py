def main():
    hello("word!!")
    goodbye("world!!")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

if __name__ == "__main()__": #if you don't use this condition then while importing main will always get called
    main()