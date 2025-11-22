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

### 9. Multiple Statements

- We can assign multiple variables and print them together.

```python
name = input("Name: ")
city = input("City: ")

print("Hello,", name)
print("You live in", city)
```

- This introduces the idea of writing programs with multiple inputs and multiple operations.

\*_Important_

- When using concatenation ("Hello, " + name), we must add spaces ourselves because the entire expression becomes one single argument.
- But when we separate items with commas in print():

```python
print("Hello,", name)
```

- Python automatically inserts a space between them because each item is treated as a separate argument to the print() function.
- This makes comma-separated printing cleaner and safer than manual string concatenation.

### 10. Pseudocode

Pseudocode is a **plain-language outline** of what a program should do before writing the actual code.  
It is not real code — just a step-by-step description of the logic.

Useful for:

- Understanding the flow of a program
- Planning before coding
- Reducing bugs by thinking through logic first

Example pseudocode for asking a name and printing a greeting:

- ask user for their name
- store the name
- print a greeting using the name

```css
Pseudocode helps convert ideas → logic → actual Python code.
```

### 11. f-Strings (Formatted Strings)

Another way to combine text and variables is by using **formatted string literals**, also called **f-strings**.

Example:

```python
name = input("What is your name? ")
print(f"Hello {name}")
```

- The f before the string allows us to directly insert variables inside { }.
- This is cleaner and easier to read than concatenation or comma-separated printing.

#### Additional Formatting with f-Strings

f-strings can also format numbers in different ways.
**1. Adding commas to large numbers**
If you have a large integer and want to display it with commas:

```python
num = 1000000
print(f"{num:,}")
```

Output:

```python
1,000,000
```

**2. Formatting floating-point numbers**
You can round a float to a specific number of decimal places using:

```python
value = 3.14159
print(f"{value:.2f}")
```

Explanation:

- .2 → round to 2 decimal places
- f → format as a floating point number

Output:

```python
3.14
```

These formatting options make f-strings very powerful for displaying clean, readable output.

### 12. Useful String Functions

Python provides several built-in string functions to clean and format user input.

---

#### `.strip()`

Removes any **leading and trailing whitespace**.

```python
name = name.strip()
```

#### .capitalize()

Capitalizes only the first letter of the string.

```python
name = name.capitalize()
```

#### .title()

Capitalizes the first letter of every word.

```python
name = name.title()
```

### 13. Chaining Methods

String methods can be combined for cleaner and more efficient code.

```python
name = name.strip().title()
```

This removes extra spaces and applies proper capitalization in one line.

### 14. Splitting Strings — .split()

.split() breaks a string into multiple parts based on a delimiter (default is space).

```python
first, last = name.split(" ")
```

This extracts the first and last name separately.

### 15. Integers (`int`)

`int` is a data type in Python used to represent **whole numbers** (positive, negative, or zero).

Example:

```python
x = 5
y = -2
z = 0
```

### 16. Integer Operations

In Python, `int` supports several arithmetic operations:

- `+` (addition)
- `-` (subtraction)
- `*` (multiplication)
- `/` (division — always returns float)
- `%` (modulus — remainder)

Example:

```python
x = 10
y = 3
print(x + y, x - y, x * y, x / y, x % y)
```

### 17. Interactive Mode (Python Interpreter)

- Python provides an interactive mode (also called the Python REPL(Read, Evaluate , Print , Loop)) where code is interpreted and executed immediately.
- You can open it by running:

```python
python
```

### Features of interactive mode:

- Executes code line by line.
- Useful for quick tests and trying small expressions.
- Helps in maintaining continuity when experimenting with values or operations.
- Example inside interactive mode:

```python
>>> 2 + 3
5
>>> "hello".upper()
'HELLO'
```

Interactive mode is often used for quick debugging or checking how Python behaves with certain operations.

### 18. Simple Calculator Project

- We create a simple calculator program.
- This project helps reinforce how each operator works (`+`, `-`, `*`, `/`, `%`) and how user input interacts with arithmetic in Python.

You can find the calculator file here:  
➡️ **[IntroductionToProgramming/Calculator.py](IntroductionToProgramming/Calculator.py)**

### The calculator allows us to:

- Take input from the user
- Convert the input to integers
- Perform arithmetic operations
- Display results using `print()`

It serves as a practical way to understand operators and how Python handles number calculations.

### 19. Float

A **float** is a data type used to store numbers with decimal points.

Example:

```python
x = 3.14
y = -2.5
z = 10.0
```

Floats allow Python to represent fractional values, unlike integers which store only whole numbers.

### 20. round() Function

Python provides the built-in round() function to round a floating-point number.

Official Python documentation syntax:

```scss
round(number[, ndigits])
```

- The square brackets [] mean optional argument.
- number → the value to round
- ndigits → (optional) how many decimal places to round to

Examples:
Without ndigits (rounds to nearest whole number):

```python
round(3.6)      # 4
round(3.2)      # 3
```

With ndigits (rounds to specific decimal place):

```python
round(3.14159, 2)   # 3.14
round(7.856, 1)     # 7.9
```

ndigits lets us control the precision — for example:

- 1 → tenths
- 2 → hundredths
- 0 → tens (python returns float e.g., round(67, -1) rounds to tens place)

### 21. Functions

In Python, we can create our own functions using the keyword **`def`**, which stands for _define_.  
Functions allow us to group code together so it can be reused whenever needed.

Basic structure:

```python
def function_name():
    # code block
```

- def → used to define a new function
- function_name → the name we choose for our function
- () → parentheses used when defining and calling functions
- : → indicates the start of the function block
- The code inside the function must be indented

Example:

```python
def hello():
    print("Hello!")
```

To run the function, we call it:

```python
hello()
```

Functions help avoid repetition and make the program cleaner, readable, and easier to maintain.

### 22. Function Order & Using `main()`

If we define a user function _at the bottom of the file_ and try to call it **before it's defined**, Python will give an error saying the function does not exist.

This happens because Python reads code **from top to bottom**, so it must encounter the function definition _before_ it is called.

To solve this, we follow a common structure:

1. Put the main logic inside a `main()` function
2. Define other functions **above or below** — order doesn't matter
3. Call `main()` at the end of the file

This ensures Python always knows what to execute first.

Example:

```python
def main():
    name = input("What is your name? ")
    hello(name)

def hello(name):
    print(f"Hello, {name}")

main()
```

- main() contains the program flow
- hello() can be written anywhere in the file
- Calling main() at the bottom starts the program

### 23. Scope of a Variable

The _scope_ of a variable refers to **where the variable is accessible** in the program.

In Python:

- A variable created **inside a function** is called a **local variable**
- It can only be used _inside that function_
- Outside the function, the variable does **not** exist

Example:

```python
def hello():
    name = "Aryan"   # local variable
    print(name)

hello()
print(name)   # ❌ Error: name is not defined
```

Variables defined outside functions are global, but using too many globals is not recommended.
Always prefer local variables for cleaner, safer code.

### 24. return Statement

The return statement is used inside a function to send a value back to the place where the function was called.

- print() → shows something on the screen
- return → gives back a value so it can be stored or used later

```python
def square(x):
    return x * x

result = square(5)
print(result)   # 25
```

## Important points:

After return executes, the function stops immediately

- A function can return:
- numbers
- strings
- lists
- booleans
- or even nothing (returns None)

### Example of stopping after return:

```python
def test():
    return 10
    print("This will never run")  # unreachable code
```

- Using return makes functions more reusable because they can give back values instead of just printing them.
