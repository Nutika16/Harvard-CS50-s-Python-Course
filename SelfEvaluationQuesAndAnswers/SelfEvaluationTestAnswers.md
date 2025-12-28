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
