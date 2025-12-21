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

### 25. Conditionals

Conditionals help us make decisions in a program.  
They allow code to execute **only when certain conditions are true**.

---

#### Comparison Operators

Python provides the following operators to compare values:

- `<` (less than)
- `>` (greater than)
- `<=` (less than or equal to)
- `>=` (greater than or equal to)
- `==` (equal to)
- `!=` (not equal to)

These operators are used inside conditional statements.

---

### `if`, `elif`, `else`

- `if` → runs **only when the condition is true**
- `elif` → runs when the previous conditions were false, but this one is true
- `else` → runs when **none** of the conditions are true

Basic structure:

```python
if condition:
    # code
elif another_condition:
    # code
else:
    # code
```

### Logical Operators: and, or

Logical operators allow us to combine multiple conditions.

**and**
All conditions must be true for the whole expression to be true.

**or**
Only one condition needs to be true for the expression to be true.

### 26. `match` Statement

Python also provides a `match` statement (introduced in Python 3.10) which works similar to a **switch-case** in other languages.  
It is used to compare a value against several patterns and execute the matching block.

Basic structure:

```python
match variable:
    case value1:
        # code
    case value2:
        # code
    case _:
        # default case
```

- match → checks the variable
- case → pattern/value to compare
- \_ → wildcard (acts like “else”), matches anything

### 27. Loops

Loops allow us to repeat a block of code multiple times without writing it again and again.  
Python mainly provides **two types of loops**: `while` loop and `for` loop.

---

### `while` Loop

A `while` loop continues running **as long as** the condition remains true.

Basic structure:

```python
while condition:
    # repeated code
```

**Important:**

- Must update the variable inside the loop
- Otherwise it becomes an infinite loop

### for Loop

A for loop is used to iterate over a sequence, such as:

- a range of numbers
- a string
- a list

Basic Structure:

```python
for item in sequence:
    # repeated code
```

### Using range()

The range() function is commonly used with loops.
Example:

```python
for i in range(3):
    print("Hello")
```

Output:

```python
Hello
Hello
Hello
```

### Looping Over Strings

Example:

```python
for char in "Aryan":
    print(char)
```

- break and continue (Optional basics)
- break → exits the loop immediately
- continue → skips the current iteration and moves to the next

Example:

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

Loops allow us to perform repeated tasks efficiently and reduce code repetition.

### 28. Lists in Python

A **list** in Python is a data structure used to store multiple values in a single variable.  
Lists are **ordered**, **changeable (mutable)**, and can hold **different data types** together.

Example:

```python
numbers = [1, 2, 3, 4]
names = ["Aryan", "Rahul", "Kumar"]
mixed = [1, "Hello", 3.14]
```

**Key Properties of Lists**

- Ordered → items have fixed positions (indexing starts at 0)
- Mutable → you can change, add, or remove items
- Allow duplicates → same value can appear more than once
- Can store different data types → int, str, float, etc.

**Assessing elements:**

### 1. Use Indexing

```python
names = ["Aryan", "Rahul", "Kumar"]
print(names[0])   # Aryan
print(names[2])   # Kumar
```

### 2. Negative Indexing

```python
print(names[-1])  # last element → Kumar
```

### 3. Modifying List Elements

```python
numbers = [10, 20, 30]
numbers[1] = 25
print(numbers)    # [10, 25, 30]
```

### 4. Common List Methods

- .append(x) → adds item to end
- .insert(i, x) → adds item at position
- .remove(x) → removes first occurrence
- .pop() → removes last item
- .sort() → sorts list
- .reverse() → reverses list

### 5. Looping through a list

```python
for item in fruits:
    print(item)
```

### 29. Dictionaries (dict)

A **dictionary** is a data structure in Python that allows us to **associate one value with another**.  
It stores data in **key–value pairs**, where each key maps to a specific value.

Example:

```python
student = {"name": "Aryan", "age": 20, "grade": "A"}
```

- "name" → key
- "Aryan" → value
- Keys must be unique
- Values can be of any data type

### Key Properties of Dictionaries

- Key–Value mapping
- Unordered (Python 3.7+ keeps insertion order)
- Mutable → values can be changed
- Keys must be immutable types (strings, numbers, tuples)

**1. Accessing Values**
Use the key:

```python
print(student["name"])     # Aryan
print(student["age"])      # 20
```

**2. Modifying a Dictionary**

```python
student["age"] = 21
```

**Adding a new key–value pair:**
student["city"] = "Delhi"

### Common Dictionary Methods

- .get(key) → safely get value
- .keys() → list of keys
- .values() → list of values
- .items() → list of key-value pairs

Example:

```python
for key, value in student.items():
    print(key, value)
```

### 30. Exceptions

An **exception** is an event that occurs while the program is running and **disrupts the normal flow** of execution.

Examples include:

- Dividing by zero
- Converting invalid input
- Accessing out-of-range list index

Python stops the program when an exception occurs unless we handle it.

---

### Syntax Errors vs Runtime Errors

#### **Syntax Error**

Happens when the programmer writes something invalid according to Python's rules.

Examples:

- Missing colon
- Misspelled keyword
- Incorrect indentation

These must be **fixed by the programmer** before the code can run.

Example:

```python
if x == 3
    print("Hello")
# ❌ SyntaxError (missing :)
```

### Runtime Error

Occurs while the program is running, even if the syntax is correct.

```python
x = int("abc")     # ❌ ValueError
```

We cannot always predict runtime errors, so to prevent the program from crashing, we use exception handling.

### Handling Exceptions (try / except)

We add extra code to catch errors and prevent the program from stopping.

Example:

```python
try:
    x = int(input("Enter a number: "))
    print(x)
except:
    print("Invalid input!")
```

- Code inside try runs normally
- If an error occurs → except block runs

### Handling NameError after try/except

A `NameError` after a `try`/`except` usually means the variable was never assigned because an exception occurred before the assignment finished. This is about **existence** of the variable, not scope.

**Fixes:**

- Initialize the variable before `try` (e.g., `x = None`) and check it after.
- Use `try` / `except` / `else` and reference the variable only in `else`.
- Use a loop to repeatedly ask for input until valid (recommended for user input).

### 31. `pass` Keyword

The `pass` keyword is used when a statement is required syntactically,  
but you don’t want to write any code there **yet**.

It acts as a **placeholder** so the program doesn’t throw an error.

Example:

```python
def todo():
    pass    # code will be written later
```

**pass does nothing — it simply allows the program to run without errors.**

### 32. raise Keyword

The raise keyword is used to manually trigger an exception in Python.

You use raise when:

- You want to signal that something went wrong
- You want to enforce rules
- You want to stop execution at a certain condition

Example:

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

Here:

- We purposely “raise” a ValueError
- The message helps identify the error

raise stops the program immediately unless handled using try/except.

### 33. Libraries and Modules

In Python, a **module** is a file that contains reusable code — such as functions, variables, or classes.  
A **library** is a collection of modules that provide additional features beyond the basic language.

Modules help us:

- Organize code
- Reuse code across programs
- Access pre-written functionality
- Keep programs clean and modular

---

### Importing Modules

We use the `import` keyword to bring a module into our program.

Example:

```python
import math
```

Now we can use anything inside the math module:

```python
print(math.sqrt(25))
```

### Using Aliases

We can rename a module or function using as:

```python
import math as m
print(m.sqrt(25))
```

or

```python
from math import sqrt as s
print(s(25))
```

Aliases help shorten long module names.

### Built-in Modules Example: random

```python
import random
num = random.randint(1, 10)
print(num)
```

- random.randint(a, b) returns a random integer between a and b.

```python
import random
coin = random.choice(["heads" , "tails"]) # choice is the function and it only takes seq i.e. lists
print(coin)
```

### Importing Specific Functions

Instead of importing the whole module, we can import only what we need:

```python
from math import sqrt
print(sqrt(25))
```

### Creating Your Own Module

Any .py file can act as your own module.

Example:

- helpers.py

```python
def greet(name):
print(f"Hello, {name}")
```

- main.py

```python
import helpers
helpers.greet("Aryan")
```

### 34. `statistics` Library

Python comes with a built-in library called **statistics**, which allows us to easily perform common statistical calculations like:

- **mean** (average)
- **median** (middle value)
- **mode** (most frequent value)

These functions save time because we don’t need to write the logic ourselves.

---

### Importing the Statistics Module

```python
import statistics
```

### Calculating Mean

```python
numbers = [10, 20, 30]
print(statistics.mean(numbers))   # Output: 20
```

### Calculating Median

```python
numbers = [10, 20, 30, 40]
print(statistics.median(numbers))   # Output: 25
```

### Calculating Mode

```python
numbers = [1, 2, 2, 3]
print(statistics.mode(numbers))     # Output: 2
```

### Shortcut: Importing Specific Functions

```python
from statistics import mean, median, mode
print(mean([1, 2, 3]))
```

### 35. Command-Line Arguments (`sys` Module)

Python programs can also receive input through the **command line**, not just through `input()`.  
For this, we use the built-in **`sys` module**.

Command-line arguments allow us to pass values to a Python script **when running it**, like:

python hello.py Aryan

````yaml

Here, `"Aryan"` is a command-line argument.

---

### Importing sys

```python
import sys
````

### Accessing Command-Line Arguments

All command-line arguments are stored in a list called:

```python
sys.argv
```

- sys.argv[0] → the name of the script
- sys.argv[1] → first argument
- sys.argv[2] → second argument and so on..........

argv stands for argument vector

Example:

```python
import sys
print(sys.argv)
```

Running:

```ngix
python greet.py Aryan Kumar
```

Output:

```css
['greet.py', 'Aryan', 'Kumar']
```

### Using Arguments in a Program

```python
import sys

if len(sys.argv) < 2:
    print("Missing argument")
else:
    print(f"Hello, {sys.argv[1]}")
```

Explanation:

- len(sys.argv) tells how many arguments were passed
- We avoid errors by checking the length first

### Handling Errors with Command-Line Arguments

If we try to access an argument that isn’t given:

```python
sys.argv[1]
```

Python will raise

```ngix
IndexError
```

So, we are checking before using it to avoid crashes

```python
if len(sys.argv) < 2:
    print("Please provide a name")
    sys.exit()
```

### Exiting the Program

sys.exit() ends the program immediately.

**Command-line arguments are useful for making scripts that can be automated, scheduled, or run with different inputs without changing the code.**

### 36. Slicing

Slicing allows us to extract a **portion** (a slice) of a sequence such as:

- strings
- lists
- tuples

The general slice syntax is:

sequence[start : end]

```csharp

- `start` → index where the slice begins (inclusive)
- `end` → index where the slice stops (exclusive)
```

Example with a string:

```python
name = "Aryan"
print(name[0:3])    # Ary
```

### Omitting Start or End

If start is omitted, it begins from the start of the sequence:

```python
name[:2]    # Ar
```

If end is omitted, it slices till the end:

```python
name[2:]    # yan
```

### Using Negative Indexes

Negative indexes count from the end:

```python
name = "Aryan"
print(name[-3:])    # yan
```

### Slicing with Step

We can also specify a step:

```pgsql
sequence[start : end : step]
```

Example:

```python
text = "abcdef"
print(text[0:6:2])   # ace
```

### Slicing Lists

Example:

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])    # [20, 30, 40]
```

Slicing is powerful for extracting specific parts of sequences in an efficient and readable way.

### 37. Packages

A **package** is a collection of third-party modules that are not included in Python by default.  
These packages provide additional functionality that we can install and use in our programs.

Examples:

- `pandas` → data analysis
- `numpy` → numerical computing
- `requests` → HTTP requests
- `flask` → web development

---

### Installing Packages

We use **pip**, Python’s package manager, to install packages.

Example:

```bash
pip install requests
```

This downloads and installs the package so it can be used in your Python code.

### Using Installed Packages

Once installed, import them like any other module:

```python
import requests
response = requests.get("https://example.com")
print(response.status_code)
```

### List All Installed Packages

```python
pip list
```

### Upgrade a Package

```python
pip install --upgrade package_name
```

### 38. Unit tests

Unit testing is a method of testing **individual parts (units)** of your code — usually functions — to ensure they work correctly.

Python provides a built-in module called **unittest** to write and run these tests.

Unit tests help in:

- Catching bugs early
- Ensuring functions behave as expected
- Preventing future changes from breaking existing code
- Making code more reliable and maintainable

---

### Creating a Unit Test

A unit test file usually:

- Imports `unittest`
- Imports the function(s) you want to test
- Contains test classes with test methods

### Common Assertions in unittest

- assertEqual(a, b) → checks if a == b
- assertNotEqual(a, b)
- assertTrue(x)
- assertFalse(x)
- assertRaises(error_type)

Example:

```python
self.assertRaises(ValueError, square, "abc")
```

**Unit testing is an important habit in professional development and ensures your code remains correct as it grows.**

### 39. File I/O (Input / Output)

File I/O refers to **reading from** and **writing to** files using Python.  
This helps us store data permanently instead of only keeping it in memory.

Python provides the built-in `open()` function to work with files.

---

### Opening a File

Basic syntax:

```python
file = open("filename.txt", "mode")
```

Common modes:

- "r" → read (default)
- "w" → write (overwrites existing file)
- "a" → append (adds to the file)
- "r+" → read and write

### Reading a File

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

- read() → reads entire file as a single string
- Using with automatically closes the file

### Read line-by-line:

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### Writing to a File

```python
with open("data.txt", "w") as file:
    file.write("Hello, world!")
```

-
- "w" creates the file if it doesn't exist
- "w" overwrites existing content

### Appending to a file:

```python
with open("data.txt", "a") as file:
    file.write("\nNew line added.")
```

### Writing Multiple Lines

```python
lines = ["Apple\n", "Banana\n", "Cherry\n"]

with open("fruits.txt", "w") as file:
    file.writelines(lines)
```

**Safest Way: Using with**

- Using with open(...) is recommended because:
- File closes automatically
- Prevents memory leaks
- Cleaner and more readable

**File I/O is essential for saving data, reading configuration files, logs, reports, and many real-world applications.**

### 40. CSV Handling (Reader, DictReader, DictWriter)

CSV (Comma-Separated Values) files are widely used for storing tabular data.  
Python provides the built-in **csv** module to read and write CSV files easily.

---

### Importing the CSV Module

```python
import csv
```

### 40.1 csv.reader

The reader class reads CSV files row-by-row as lists.

Example:

```python
import csv

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

If students.csv contains:

```python
Aryan,20,CS
Rahul,21,IT
```

Output:

```python
['Aryan', '20', 'CS']
['Rahul', '21', 'IT']
```

- Each row is returned as a list
- Columns remain positional (indexed)

### 40.2 csv.DictReader

DictReader reads each row as a dictionary where keys come from the header row.

Example:

```python
import csv
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

If the file contains:

```python
name,age,branch
Aryan,20,CS
Rahul,21,IT
```

Output:

```bash
{'name': 'Aryan', 'age': '20', 'branch': 'CS'}
{'name': 'Rahul', 'age': '21', 'branch': 'IT'}
```

Advantages:
Easier to access using column names:

```python
print(row["name"])
```

- Makes code more readable than positional indexing

### 40.3 csv.DictWriter

DictWriter writes data as dictionaries, automatically using keys as headers.
Example:

```python
import csv

with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "branch"])
    writer.writeheader()  # writes: name,age,branch

    writer.writerow({"name": "Aryan", "age": 20, "branch": "CS"})
    writer.writerow({"name": "Rahul", "age": 21, "branch": "IT"})
```

This will produce:

```pgsql
name,age,branch
Aryan,20,CS
Rahul,21,IT
```

**Important:**

- fieldnames must match the keys in each dict
- writeheader() writes the first row (column names)

### 40.4 When to Use What?

| Class        | Use Case                                                  |
| ------------ | --------------------------------------------------------- |
| `reader`     | When the CSV has **no header** or structure is simple     |
| `DictReader` | When file has **column names** and you want readable code |
| `DictWriter` | When writing data using **dictionaries** for clarity      |

**Handling CSVs is extremely common in data processing, automation scripts, reporting, and backend development.**

### 41. PIL (Pillow)

**PIL** stands for _Python Imaging Library_.  
Its modern version is called **Pillow** — a powerful library used to perform operations on image files.

To install:

```bash
pip install pillow
```

### Importing Pil

```python
from PIL import Image
```

### Common Uses of Pillow

**Pillow allows you to:**

- Open images
- Resize images
- Crop image
- Convert image formats (PNG → JPG, etc.)
- Rotate and flip images
- Create thumbnails
- Save modified images

### Opening an Image

```python
from PIL import Image

img = Image.open("photo.jpg")
img.show()
```

### Resizing an Image

```python
img = Image.open("photo.jpg")
resized = img.resize((300, 300))
resized.save("photo_resized.jpg")
```

### Converting Image Format

```python
img = Image.open("photo.png")
img.save("photo.jpg")
```

### Cropping an Image

```python
img = Image.open("photo.jpg")
cropped = img.crop((0, 0, 200, 200))
cropped.save("photo_cropped.jpg")
```

### Creating Thumbnail

```python
img = Image.open("photo.jpg")
img.thumbnail((150, 150))
img.save("photo_thumbnail.jpg")
```

**Pillow is widely used in:**

- Web development
- Automation scripts
- Data preprocessing
- Machine learning (image-based models)
- It provides simple functions to manipulate and process image files efficiently.

### 42. Regular Expressions (Regex)

Regular expressions (also called **regexes**) are used to **find, match, or validate patterns** in text.

They are commonly used to:

- Validate user input (email, phone number, password)
- Search for specific patterns in text
- Extract required information from strings

Python provides a built-in library called **`re`** to work with regular expressions.

---

### Importing the `re` Module

```python
import re
```

**Basic Example: Email Validation**
Suppose we want the user to enter an email address and check whether it is valid.

```python
import re

email = input("Enter your email: ")

if re.search(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
    print("Valid email")
else:
    print("Invalid email")

```

**Explanation:**

- ^ → start of string
- @ → must contain @
- \. → dot (.)
- $ → end of string

**Common re Functions**

- re.search() → searches for a pattern anywhere in the string
- re.match() → checks pattern only at the beginning
- re.findall() → returns all matches as a list
- re.sub() → replaces matches with another string

Example:

```python
text = "My phone number is 9876543210"
numbers = re.findall(r"\d+", text)
print(numbers)
```

### Common Regex Quantifiers

Regular expressions use special symbols called **quantifiers** to specify how many times a character or pattern should repeat.

- `.` → Matches **any single character except a newline**
- `*` → Matches **0 or more repetitions** of the preceding pattern
- `+` → Matches **1 or more repetitions** of the preceding pattern
- `?` → Matches **0 or 1 repetition** of the preceding pattern
- `{m}` → Matches **exactly `m` repetitions** of the preceding pattern

**Why Use Regular Expressions?**

- Flexible pattern matching
- Saves time compared to manual checks
- Widely used in validation and parsing tasks
