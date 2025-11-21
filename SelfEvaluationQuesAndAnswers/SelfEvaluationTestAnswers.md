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
