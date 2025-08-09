# Python for Web Developers Learning Journal

## Exercise 1.3: Operators & Functions in Python

### Reflection Questions

---

**In this Exercise, you learned how to use if-elif-else statements to run different tasks based on conditions that you define. Now practice that skill by writing a script for a simple travel app using an if-elif-else statement for the following situation:**

- **The script should ask the user where they want to travel.**
- **The user’s input should be checked for 3 different travel destinations that you define.**
- **If the user’s input is one of those 3 destinations, the following statement should be printed: “Enjoy your stay in ...!”**
- **If the user’s input is something other than the defined destinations, the following statement should be printed: “Oops, that destination is not currently available.”**
  **Write your script here. (Hint: remember what you learned about indents!)**

```python
destinations = {"Naples", "Rome", "Venice"}
destination = input("Where would you like to go? ")

if destination in destinations:
    print(f"Enjoy your stay in {destination}!")
else:
    print("Oops, that destination is not currently available.")
```

---

**Imagine you’re at a job interview for a Python developer role. The interviewer says “Explain logical operators in Python”. Draft how you would respond.**

Logical operators in Python, as in most other programming languages, are used to combine conditional statements. There are three main ones:

1. **`and`** – Returns `True` if both conditions are true.
   Example: `x > 5 and x < 10`

2. **`or`** – Returns `True` if at least one condition is true.
   Example: `x < 5 or x > 10`

3. **`not`** – Reverses the result; returns True if the condition is false.
   Example: `not(x > 5)` If x is 3, this returns True.

Logical operators are commonly used in `if` statements to make decisions based on multiple conditions.

---

**What are functions in Python? When and why are they useful?**

Functions in Python, as in most other programming languages, are blocks of reusable code that perform a specific task. You define a function once and can use it as many times as needed.

Eexample of Python function defintion:

```python
def greet(name):
    print(f"Hello, {name}!")
```

Functions are useful because they help avoid repetition by allowing you to write code once and reuse it wherever needed. They also improve readability, making your code easier to understand and manage. Additionally, functions help organize logic by breaking complex problems into smaller, more manageable steps. This makes them especially helpful in larger programs, where clean and efficient code is essential.

---

**In the section for Exercise 1 in this Learning Journal, you were asked in question 3 to set some goals for yourself while you complete this course. In preparation for your next mentor call, make some notes on how you’ve progressed towards your goals so far.**

I am getting familiar with Python syntax. For now, we’re mostly focusing on concepts that we’ve already seen in JavaScript, but Python-specific concepts are already starting to appear. It’s probably too soon for me to say this with certainty, but I sense that Python is better suited for problem-solving—at least for the beginner-level problems I’m working on in Exercism. My interest in this language is definitely growing.
