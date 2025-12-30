## 🧠 Self-Assessment Test — My Answers & Evaluation

## Assignment 1

### ✔ Part A — Concepts

1. **Difference between concatenation and comma:**

   - `print("Hello" + name)` → concatenation, treated as **one argument**, spacing must be added manually.
   - `print("Hello", name)` → two arguments, Python automatically inserts a **space**.

2. **Side effect:**  
   A function doing something outside of returning a value. Example: `print()` displaying text on the screen.

3. **Purpose of input():**  
   Used to take user input dynamically. It always returns a **string**.

4. **Variable:**  
   A container that holds a value. It can be changed (reassigned) any time in the program.

5. **.strip():**  
   Removes leading and trailing whitespace. Often used with `input()`.

6. **round(number[, ndigits]) — square brackets meaning:**  
   The parameter is **optional**.

7. **Pseudocode:**  
   Plain-language outline of logic to plan a program and reduce bugs.

8. **f-string:**  
   A formatted string literal allowing variables inside `{}`.  
   Advantage: more readable and supports formatting inside the string.

9. **capitalize() vs title():**

   - `capitalize()` → only first letter of whole string becomes uppercase.
   - `title()` → first letter of **every word** becomes uppercase.

10. **split(" ") on "Aryan Kumar":**  
    Returns two substrings: `"Aryan"` and `"Kumar"`.

---

### ✔ Part B — Output Prediction

11. Output: 50
12. Output: Aryan
13. Output: 3.14
14. 1,000,000
15. Output: Elon
    Musk

---

### ✔ Part C - Code Writing

```python
16. name = input("What is your name? ").strip().capitalize()
print("Welcome,", name)
```

```python
17. value = float(input("Enter a float: "))
print(f"{value:.2f}")
```

## Assignment -2

## 🧠 Self-Evaluation Test – Part 2 (Answer Key)

### 📌 Part A — Concept Questions

1. **Purpose of `def`:**  
   Used to define user-defined functions in Python.

2. **Why use `main()`:**  
   To structure code properly, improve readability, and avoid calling functions before definitions. `main()` is called at the bottom to start the program flow.

3. **Local vs Global Variable:**

   - Local → accessible only inside the function/block.
   - Global → accessible throughout the program.

4. **return vs print:**

   - `return` sends a value back to the caller and ends the function.
   - `print` only displays output to the screen and returns `None`.

5. **pass keyword:**  
   A placeholder used when a statement is required syntactically but no code needs to run.

6. **raise keyword:**  
   Used to manually raise exceptions.  
   Example:
   ```python
   if age < 0:
       raise ValueError("Age cannot be negative")
   ```
7. **What is a module:**
   A file containing reusable functions, variables, or classes. Imported using import module_name.

8. **statistics library:**
   Provides statistical functions like mean, median, and mode.

9. **sys.argv meaning:**

- A list of command-line arguments.
- sys.argv[0] → script name
- sys.argv[1] → first argument provided

10. **Accessing sys.argv[1] without argument:**
    Raises IndexError.

11. **Slicing:**
    Technique to extract a portion of a sequence.
    Syntax: sequence[start:end]

## 📌 Part B — Output Prediction

12. 16
13. A
14. 4
15. 2
16. Python
    amming
    PtoPormig

## 📌 Part C — Code Writing

17. _Function that returns a greeting:_

```python
def hello(name):
return f"Hello, {name}"
```

18. _Command-line argument greeting:_

```python
import sys

if len(sys.argv) < 2:
print("Missing name")
else:
print(f"Hello, {sys.argv[1]}")s
```

19. _Median using statistics:_

```python
import statistics

print(statistics.median([10, 30, 60]))
```

20. _Slicing "Introduction" into "Intro" and "duction":_

```python
name = "Introduction"

print(name[:5]) # Intro
print(name[5:]) or print(name[-7:]) # duction
```

# ✅ Assignment 3 — Answer Key

## 🧠 Self-Evaluation Test – Part 3 (Intermediate Python)

---

## 📌 Part A — Concept Answers

### 1. for loop vs while loop

A `for` loop is used when the number of iterations is known in advance, whereas a `while` loop is used when iteration depends on a condition.

---

### 2. List

A list is a data structure used to store a collection of elements.  
Key properties:

- Lists are mutable
- Lists are ordered and indexed

---

### 3. Dictionary

A dictionary is a data structure that stores data in key-value pairs.  
It differs from a list because data is accessed using keys instead of indexes, and dictionaries provide fast lookups by key.

---

### 4. Exception

An exception is a runtime error that occurs during program execution even though the syntax is correct.  
We use `try` and `except` to catch and handle exceptions gracefully.

---

### 5. Syntax error vs Runtime error

- Syntax error occurs when code violates Python syntax rules (e.g., missing parentheses).
- Runtime error occurs during execution (e.g., division by zero causing `ZeroDivisionError`).

---

### 6. pass keyword

The `pass` keyword is a null statement used as a placeholder when a statement is syntactically required but no action is needed.

---

### 7. raise keyword

The `raise` keyword is used to manually trigger an exception when a specific condition occurs.

---

### 8. File I/O and `with`

File I/O refers to reading from and writing to files stored on disk.  
The `with` statement (context manager) is recommended because it ensures automatic file closing and proper resource management.

---

### 9. csv.reader vs csv.DictReader

- `csv.reader` reads rows as lists.
- `csv.DictReader` reads rows as dictionaries using the header row as keys.

---

### 10. Package vs Module

A module is a single Python file containing code, whereas a package is a directory containing multiple related modules.

---

### 11. Regular Expressions

Regular expressions are patterns used to search, match, and manipulate text.  
The `re` module provides regex functionality in Python.

---

### 12. Unpacking

Unpacking allows assigning elements of a collection to multiple variables in a single statement.

---

### 13. map()

`map()` applies a function to each element of an iterable and returns a map object.

---

### 14. filter()

`filter()` selects elements from an iterable that satisfy a given condition.

---

### 15. List comprehension

List comprehensions are preferred because they are cleaner, more readable, and more concise.

---

### 16. Dictionary comprehension

Dictionary comprehension provides a concise way to create dictionaries.

---

### 17. enumerate()

`enumerate()` returns both the index and the value while iterating over an iterable.

---

## 📌 Part B — Output Answers

### 18.

```python
[2, 4, 6, 8]
```

### 19.

```python
[2, 4]
```

### 20.

```python
[1, 4, 9]
```

### 21.

```python
1 Aryan
2 Nutika
3 Radha
```

### 22.

```python
{'a': 2, 'b': 4}
```

### 23.

```python
10
[20, 30, 40]
```

### 📌 Part C — Code Answers

24.

```python
nums = [1, 2, 3, 4, 5, 6]
even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)
```

25.

```python
def add(*args):
    return sum(args)
```

26.

```python
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

27.

```python
count = 0

with open("data.txt") as file:
    for _ in file:
        count += 1

print("Total lines:", count)
```

28.

```python

import re

email = input("Enter email: ")

if re.search(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
    print("Valid email")
else:
    print("Invalid email")
```

29. enumerate usage

```python
items = ["apple", "banana", "cherry"]

for index, item in enumerate(items):
    print(index, item)
```

30.

```python
squares = {x: x * x for x in range(1, 6)}
print(squares)
```
