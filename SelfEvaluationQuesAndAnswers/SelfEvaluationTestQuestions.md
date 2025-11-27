## 🧠 Self-Assessment Test

## Assignment- 1

This self-evaluation test covers everything learned so far, including:

- print() function
- Arguments
- Bugs
- Side effects
- input()
- Variables
- String concatenation
- Type conversion
- Multiple statements (comma vs concatenation)
- Pseudocode
- f-strings
- String methods (strip, capitalize, title)
- Chaining methods
- split()
- Integers
- Integer operations
- Interactive mode
- Simple calculator
- Floats
- round() function

---

# ✅ SELF-EVALUATION TEST (Basics of Python)

## 📌 Part A — Concept Questions

1. **What is the difference between:**

```python
   print("Hello" + name)
   print("Hello", name)
```

2. What is a side effect? Give one example from Python.
3. What is the purpose of the input() function and what data type does it always return?
4. What is a variable? Write your own short definition.
5. What does .strip() do? When is it useful?
6. When using round(number[, ndigits]), what does the square bracket mean?
7. What is pseudocode and why do we use it?
8. What is an f-string? Write one advantage of using f-strings over concatenation.
9. What is the difference between .capitalize() and .title()?
10. What will .split(" ") do to this string?
    "Aryan Kumar"

---

### 📌 Part B — Predict the Output

11. What will this print?

```python
print("Score:", 50)
```

12. What will this print?

```python
name = "  aryan  "
print(name.strip().capitalize())
```

13. What will this print?

```python
value = 3.14159
print(f"{value:.2f}")
```

14. What will this print?

```python
num = 1000000
print(f"{num:,}")
```

15. What will this print?

```python
first, last = "Elon Musk".split(" ")
print(first)
print(last)
```

---

### 📌 Part C — Write the Code

16. Write code to:

- Ask the user for their name
- Remove extra spaces
- Capitalize it properly
- Print: "Welcome, <name>"

17. Write code to:

- Ask the user for a number
- Convert it to an integer
- Print the number rounded to the nearest whole number using round()

18. Write code to:

- Take a float from the user
- Print it rounded to two decimal places using an f-string.

## Assignment 2

## 🧠 Self-Evaluation Test – Part 2

This test covers the following topics:

- Functions (`def`)
- main() structure
- Function calling order
- Variable scope
- return statement
- pass keyword
- raise keyword
- Libraries and Modules
- statistics library (mean, median, mode)
- Command-line arguments (`sys`)
- Slicing

---

## 📌 Part A — Concept Questions

1. What is the purpose of using `def` in Python?

2. Why do we put our main program inside a function like `def main():` and call `main()` at the bottom?

3. What is the difference between a **local variable** and a **global variable**?

4. What does the `return` statement do inside a function?  
   How is it different from `print()`?

5. What does the `pass` keyword do?  
   Why would we use it?

6. What does the `raise` keyword do?  
   Give an example situation where you might use it.

7. What is a module?  
   How do we import one?

8. What does the statistics library help us calculate?  
   Name at least two functions.

9. What is `sys.argv`?  
   What does `sys.argv[0]` and `sys.argv[1]` represent?

10. What happens if you try to access `sys.argv[1]` but the user did not provide any argument?

11. What is slicing?  
    Write the general syntax for slicing a sequence.

---

## 📌 Part B — Predict the Output

12. What will this print?

```python
def square(x):
    return x * x

print(square(4))
```

13. What will this print?

```python
def test():
    print("A")
    return
    print("B")

test()
```

14. What will this print?

```python
import statistics
print(statistics.mean([2, 4, 6]))
```

15. What will this print?

```python
import sys
print(len(sys.argv))
```

(Assume the script is run as: python greet.py Aryan)

16. What will this print?

```python
name = "PythonProgramming"
print(name[0:6])
print(name[-6:])
print(name[::2])
```

###📌 Part C — Write the Code 17. Write a function hello(name) that returns (NOT prints)
"Hello, <name>".

18. Write a program using sys.argv that prints:

- "Hello, <name>" if one argument is provided
- "Missing name" if no argument is provided

19. Write code to calculate the median of a list using the statistics module.

20. Write code to slice the string "Introduction" to get "Intro" and "duction" separately.
