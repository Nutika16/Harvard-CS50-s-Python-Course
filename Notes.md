# 📘 CS50 Python – Introduction TO Programming in Pyton **Notes**

## 📝 Summary

These notes provide a structured and technically detailed overview of the concepts covered in the CS50 Python course.  
They are written to serve as a clear reference for anyone revisiting foundational Python topics, offering concise explanations, definitions, examples, and key insights.  
The goal is to create a comprehensive resource that supports learning, revision, and practical understanding of Python programming principles, regardless of prior experience level.

---

## 🔑 Key Concepts

### 1. `print()` Function

- `print()` is a **predefined (built-in) function** in Python.
- It displays output on the screen.
- Example:

```python
print("Hello, world!")
```

### 2. Arguments

Arguments are the values we pass into a function.

- In print("Hello"), the argument is "Hello".
- Arguments are written inside the parentheses of a function.
- They can be:
- Strings
- Numbers
- Variables
- Expressions

### 3. 🔍 Bugs

No matter how experienced a programmer is, mistakes will happen. These mistakes are called **bugs**.

- Bugs can occur due to:
- Wrong arguments
- Wrong syntax
- Logical mistakes

### 4. Side Effects

- A **side effect** is something a function does outside of returning a value.

Example:

- Printing to the screen
- Writing to a file
- Sending data to a server

- The print() function is a perfect example of a function whose purpose is a side effect: showing text on the screen.

### 5. input() Function

- The input() function is used to take input from the user.
- The value typed by the user is always received as a string.
- We can pass a prompt as an argument inside input().

Example:

```python
name = input("What is your name? ")
print("Hello, " + name)
```

### 📌 Points to Remember so far.

1. print() shows output → side effect.
2. input() collects user input → argument is the question prompt.
3. Bugs are normal in coding; they help us learn.
4. Python functions are powerful and rely heavily on arguments.

### 6. Variables

A **variable** is a named location in memory that stores a value.  
In Python, a variable is created automatically when you assign a value to it.

Example:

```python
name = input("What is your name? ")
```

Here:

- name → variable
- = → assignment operator
- input("What is your name? ") → value stored inside the variable

### Key points about variables:

- They hold data so it can be used later.
- The value of a variable can change (hence the name “variable”).
- Variables should have meaningful names for readability.

### 7. String Concatenation

Since input() always returns a string, combining it with another string is called concatenation.
Example:

```python
print("Hello, " + name)
```

Python joins the two strings into:
Hello, <user_input>

### Important:

If you try to add a string and an integer without converting, Python will show a TypeError.

**Example (❌ wrong):**

```python
print("You are " + age)
```

**Example (✔ correct):**

```python
print("You are " + str(age))
```

### 8. Comments in Python

- Comments help document your code for yourself and others.
- Python ignores comments during execution.

### Single line comment

```python
# This is a comment
```

### Why comments matter:

- Improve readability
- Help explain logic
- Useful for debugging
- Good practice in professional codebases
