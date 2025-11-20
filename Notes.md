# 📘 CS50 Python – Introduction & First Program

## 📝 Summary

In this section, I wrote my first Python program and learned about basic functions, user input, arguments, bugs, and side effects. These concepts form the foundation for everything that comes next in Python programming.

---

## 🔑 Key Concepts

### 1. `print()` Function

- `print()` is a **predefined (built-in) function** in Python.
- It displays output on the screen.
- Example:

```python
print("Hello, world!")
```

## 2. Arguments

Arguments are the values we pass into a function.
In print("Hello"), the argument is "Hello".
Arguments are written inside the parentheses of a function.
They can be:
-Strings
-Numbers
-Variables
-Expressions

## 3. 🔍 Bugs

No matter how experienced a programmer is, mistakes will happen.
These mistakes are called bugs.
Bugs can occur due to:
-Wrong arguments
-Wrong syntax
-Logical mistakes

## 4. Side Effects

A side effect is something a function does outside of returning a value.

Example:
-Printing to the screen
-Writing to a file
-Sending data to a server

The print() function is a perfect example of a function whose purpose is a side effect: showing text on the screen.

## 5. input() Function

-The input() function is used to take input from the user.
-The value typed by the user is always received as a string.
-We can pass a prompt as an argument inside input().

Example:

````python
name = input("What is your name? ")
print("Hello, " + name)
```s

📌 Points to Remember so far.

1. print() shows output → side effect.
2. input() collects user input → argument is the question prompt.
3. Bugs are normal in coding; they help us learn.
4. Python functions are powerful and rely heavily on arguments.
````
