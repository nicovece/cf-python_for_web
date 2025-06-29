# Python for Web Developers Learning Journal

## Pre-Work: Before You Start the Course

_Reflection questions (to complete before your first mentor call)_

---

**What experiences have you had with coding and/or programming so far? What otherå experiences (programming-related or not) have you had that may help you as you progress through this course?**

I have been working as a freelance designer and front-end developer since 2005, mainly on small projects. I am self-taught and have strong skills in HTML and CSS, along with some experience using JavaScript and PHP for basic tasks.

Over the years, I’ve learned to take full responsibility for my work and have developed solid problem-solving skills. I’m comfortable handling difficult situations, whether working alone or as part of a team. My former mentor also mentioned that this experience was especially valuable during my full-stack immersion course.

---

**What do you know about Python already? What do you want to know?**

I have completed an introductory course in Python. I learned about the fundamentals of the language, including basic data types, container types, functions, boolean logic, loops, and control statements. I also wrote some very simple programs.

---

**What challenges do you think may come up while you take this course? What will help you face them? Think of specific spaces, people, and times of day of week that might be favorable to your facing challenges and growing. Plan for how to solve challenges that arise.**

I expect to face some challenges during this course, although I’m not entirely sure what they will be yet. One challenge I can already foresee is that this will be my first time working with technologies beyond HTML, CSS, and JavaScript. While that’s a bit outside my comfort zone, I find it exciting.

What will help me face these challenges is my curiosity and willingness to learn, along with the experience I've gained from solving problems independently as a freelancer. I also believe that challenges are essential for growth—if everything goes too smoothly, it quickly becomes uninteresting.

---

## Exercise 1.1: Getting Started with Python

### Reflection Questions

---

**In your own words, what is the difference between frontend and backend web development? If you were hired to work on backend programming for a web application, what kinds of operations would you be working on?**

Frontend and backend development can be compared to a restaurant. The frontend is like the waiter—interacting with customers and presenting the menu. It’s what users see and use, built with HTML, CSS, and JavaScript.

The backend is like the kitchen staff—working behind the scenes to prepare the food. In web development, this means handling data, server logic, authentication, and database communication.

If I were hired for backend programming, I’d work on things like building APIs, managing databases, and ensuring the server supports what the frontend needs.

---

**Imagine you’re working as a full-stack developer in the near future. Your team is asking for your advice on whether to use JavaScript or Python for a project, and you think Python would be the better choice. How would you explain the similarities and differences between the two languages to your team? Drawing from what you learned in this Exercise, what reasons would you give to convince your team that Python is the better option?**

Both JavaScript and Python are versatile, high-level languages with strong communities. JavaScript is mainly used for frontend and also works on the backend with Node.js, while Python is known for its clean syntax and is widely used in backend development, especially for tasks involving data or automation.

Without knowing the project's specifics, it's hard to make a definitive choice. However, based on what I’ve learned, I’d lean toward Python for its readability, fast development with frameworks like Django or Flask, and strong support for backend logic and data handling.

---

**Now that you’ve had an introduction to Python, write down 3 goals you have for yourself and your learning during this Achievement. You can reflect on the following questions if it helps you. What do you want to learn about Python? What do you want to get out of this Achievement? Where or what do you see yourself working on after you complete this Achievement?**

- I want to continue learning as much as I can about Python—not just during this course, which would be impossible to cover everything, but throughout my career.
- I aim to gain a solid understanding of a tool that requires a completely new mindset and approach for me.
- Realistically, I see myself working on web-based projects, as that has been my focus for years. However, I hope to dive deeper into software development and eventually move beyond the web to work more on general-purpose software.

---

## Exercise 1.2: Data types in python

### Reflection Questions

---

**Imagine you’re having a conversation with a future colleague about whether to use the iPython Shell instead of Python’s default shell. What reasons would you give to explain the benefits of using the iPython Shell over the default one?**

IPython offers syntax highlighting and auto-indentation, making code easier to read and write. It also includes features like tab-completion, object introspection (`?` for help), magic commands (e.g., `%time`), and clearer tracebacks, making it more efficient and user-friendly than the default Python shell.

---

**Python has a host of different data types that allow you to store and organize information. List 4 examples of data types that Python recognizes, briefly define them, and indicate whether they are scalar or non-scalar.**

**`float` (Floating-Point Number):**

- Represents numbers with a decimal point, or in exponential form.
- Scalar
- Example: `3.14`, `-0.001`, `2.5e2` (which is 2.5 x 10² = 250)

  **`tuple`**

- An ordered collection of items, similar to a list. However, tuples are immutable, meaning you cannot change their contents once they are created. They are defined by having values between parentheses `()`
- Non-scalar
- Example from your file: `(2008, 6789088686)`

**`dict` (Dictionary)**

- An unordered collection of key-value pairs. Dictionaries are mutable and are used to store data values like a map. They are enclosed in curly braces `{}`
- Non-scalar
- Example: `{"name": "Alice", "age": 30}`

**`set`**

- An unordered collection of unique items. Sets are mutable, and you can add or remove items from them. They are also enclosed in curly braces `{}`. Any duplicate items are automatically removed.
- Non-scalar
- Example: `{1, 2, "hello"}`

---

**A frequent question at job interviews for Python developers is: what is the difference between lists and tuples in Python? Write down how you would respond.**

In Python, lists are mutable, meaning you can change their content (add, remove, or modify elements), while tuples are immutable—you can't change them after creation. Because of this, tuples are often used for fixed data and can be slightly faster and safer than lists in certain situations.

---

**In the task for this Exercise, you decided what you thought was the most suitable data structure for storing all the information for a recipe. Now, imagine you're creating a language-learning app that helps users memorize vocabulary through flashcards. Users can input vocabulary words, definitions, and their category (noun, verb, etc.) into the flashcards. They can then quiz themselves by flipping through the flashcards. Think about the necessary data types and what would be the most suitable data structure for this language-learning app. Between tuples, lists, and dictionaries, which would you choose? Think about their respective advantages and limitations, and where flexibility might be useful if you were to continue developing the language-learning app beyond vocabulary memorization.**

For the language-learning app, a **list of dictionaries** would be the most suitable data structure.

Each flashcard can be represented as a **dictionary**, where the keys describe the data (`"word"`, `"definition"`, `"category"`). The entire set of flashcards would then be stored in a **list**.

Example:

```python
flashcards = [
    {
        "word": "ephemeral",
        "definition": "Lasting for a very short time.",
        "category": ["adjective"]
    },
    {
        "word": "run",
        "definition": "Move at a speed faster than a walk.",
        "category": ["verb", "noun"]
    }
]
```

Using a list of dictionaries for flashcards offers clarity, flexibility, and extensibility. Accessing values by keys (e.g., card['word']) is more readable and less error-prone than using indexes. Both the list and the dictionaries are mutable, allowing easy updates, additions, or deletions. This structure also supports features like multiple categories per word and can easily be extended with new fields like example sentences or images. In contrast, tuples are immutable and harder to update, while lists of lists are more error-prone and less readable.

---

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
