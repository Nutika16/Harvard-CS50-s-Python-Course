def main():
    yell("This" , "is", "nutika")

def yell(*words):
    # uppercased = map(str.upper, words)
    ''' we can do the exact same thing using list comprehension'''
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()