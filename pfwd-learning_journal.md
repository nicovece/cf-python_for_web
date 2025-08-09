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

---

---

## Exercise 1.4: File Handling in Python

### Reflection Questions

---

**Why is file storage important when you're using Python? What would happen if you didn't store local files?**

File storage is important in Python, and in programming in general, because it allows data to persist after the program has finished running. Without storing data in files, all information would be lost when the program ends, making it impossible to save user input, results, or any progress between sessions.

Additionally, storing data in files makes it possible to share information between different programs or users, or to transfer data from one system to another. This is essential for collaboration, backups, and integrating with other tools or platforms.

---

**In this Exercise you learned about the pickling process with the pickle.dump() method. What are pickles? In which situations would you choose to use pickles and why?**

The Python pickle process is used to save ("serialize" with `pickle.dump(obj, file)`) and load ("deserialize" with `pickle.load(file)`) Python objects by converting them into a format that can be stored on disk. This process is called serialization (or pickling). It turns objects like lists, dictionaries, or custom classes into a byte stream. This byte stream contains all the details needed to rebuild the object later in another Python program. The reverse process, called deserialization (or unpickling), restores the object to its original form.

Situations suitable for Pickles use:

- **Saving program state**: For example, saving a trained machine learning model, or the progress of a game, or a Python session's data.
- **Caching**: Store expensive computations or data fetched from APIs locally so you don't have to re-fetch or re-calculate.
- **Passing complex data between Python programs**: If you need to send data between processes or across a network (with some caveats—see below).
- **Quick data persistence for internal tools**: When you're building tools/scripts for personal use or prototyping, and you need a quick way to store Python objects.

---

**In Python, what function do you use to find out which directory you're currently in? What if you wanted to change your current working directory?**

Using the os module command `os.getcwd()`, you can find out which directory you are currently working in. To change the current working directory, you can use `os.chdir(path)`, where `path` is the new directory you want to move to.
(Os module must be imported first with `import osg.)

Example

```python
import os                 # Imports os module
print(os.getcwd())        # Shows the current working directory
os.chdir('/new/path')     # Changes to the specified directory
```

---

**Imagine you're working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?**

I would use a `try-except` block. By placing the potentially problematic code inside a `try` block, Python will attempt to run it. If there are no errors, the code inside the `try` block runs normally and the program continues as usual. If an error occurs, instead of stopping the entire script, Python will jump to the `except` block, where I can handle the error gracefully—such as by showing a helpful message to the user or taking corrective action. This way, the rest of the script can continue running.

For example:

```python
try:
    # Code that might cause an error
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero! Please check your input.")
```

It is also possible to catch all exceptions:

```python
try:
    # risky code
except Exception as e:
    print(f"An error occurred: {e}")
```

This approach helps prevent the entire script from terminating due to an error in one part of the code, while allowing normal execution if no errors occur.

---

**You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call.**

I think my learning is going pretty well. I’m encountering new, Python-specific concepts, and these are the ones I need to put more effort into understanding. They’re not particularly complex, but they are completely new to me, so I can’t rely on previous knowledge. While learning, I don’t feel pride as much as a quiet sense of fulfillment — as if my mind is slowly filling with light. It’s not tied to any one topic, but to the journey as a whole.

---

---

## Exercise 1.5: Object-Oriented Programming in Python

### Reflection Questions

---

**In your own words, what is object-oriented programming? What are the benefits of OOP?**

Object-oriented programming is a way of writing code where we think of things as **objects** — like real-world things. For example, if you’re making a game, you might have objects like a **Player**, **Enemy**, or **Score**. Each object has:

- **Attributes** (also called properties) – things it _has_, like a player's name or health.
- **Methods** – things it _can do_, like move or attack.

We use **classes** to create these objects. A class is like a blueprint, and the object is built from that blueprint.

The benefits of OOP are:

- **Organized code** – It’s easier to group related code together in one place (in a class).
- **Reusability** – You can reuse classes in other programs without rewriting them.
- **Easier to update** – If something changes, you only need to update the class, not every place the object is used.
- **Encapsulation** – You can hide the details of how something works and only show what’s necessary. This keeps things simple and safe.
- **Inheritance** – You can create a new class based on an existing one, saving time and reducing code duplication.

---

**What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.**

A class is like a blueprint or a recipe. It defines what something is and what it can do. An object is a specific thing made from that class, an instance. It follows the blueprint but has its own unique data.

An example is the samrtphone.

**Class** : Smartphone
This is the **blueprint** for any phone. It defines what every smartphone _has_ (like brand, model, storage) and what it _can do_ (make calls, take photos, send messages).

**Object / Instance**: My iPhone
Each actual phone is a unique object created from the `Smartphone` class. It might have a different brand, color, or amount of storage — but it still works like a phone.

---

**In your own words, write brief explanations of the following OOP concepts; 100 to 200 words per method is fine.**

**Inheritance**
Inheritance allows one class (called a child class or subclass) to take on the features of another class (called the parent class or superclass). It helps us reuse code, organize it better, and avoid repetition.

For example, imagine a Vehicle class with basic features like speed and color. A Car or Bike can inherit from Vehicle, meaning they automatically get all its features. However, they can also have their own unique features, such as the number of doors for a car or the type of handle for a bike.

Inheritance makes programs more flexible and easier to maintain. If we update something in the parent class, the changes automatically apply to all child classes. This saves time and reduces errors when modifying or expanding our code.

**Polymorphism**
Polymorphism allows different classes to define their own version of a method with the same name, and the correct version is chosen automatically depending on the object. This makes our code more flexible and easier to extend.

A good example is a payment system. Imagine we're building a shopping app that supports different payment types: Credit Card, PayPal, and Cryptocurrency. Each payment type has a process_payment() method, but it behaves differently depending on the method used.

We could have a PaymentMethod parent class, with subclasses for each type, such as CreditCard or PayPal. All subclasses use the same method name: process_payment(), but each class defines it differently based on how that payment method works. Other parts of the app can simply call the method without needing to know which type of payment is being used — they’ll just get the correct result.

Even though the method name is the same, the behavior changes depending on the object. This is polymorphism in action. It helps us write cleaner, more adaptable code that works with many object types through shared method names.

**Operator Overloading**
Operator overloading lets us customize how Python’s built-in operators (like +, -, ==, and others) behave for our own classes. This means we can define what it means to “add” two objects, compare them for equality, or use other operators in a way that makes sense for our objects.

For example, imagine a class that represents a Book. We can decide what happens when two books are added together — perhaps combining their total number of pages or appending the content of the second book to the first.

By defining these behaviors, operator overloading makes custom objects feel more natural and easier to use, almost like built-in types in the language. It helps write cleaner and more readable code when working with complex data.

---

---

## Exercise 1.6: Databases in Python

### Reflection Questions

---

**What are databases and what are the advantages of using them?**

A database is a structured way to store, organize, and retrieve large amounts of data. We can think of it like a digital filing cabinet with multiple drawers (tables) that contain organized information.

**Key advantages of using databases:**

**Organization and Structure** - Instead of scattered files, our data follows a clear structure with defined relationships between different pieces of information.

**Efficient Storage and Retrieval** - Databases are optimized to quickly find specific data, even when dealing with millions of records. Much faster than searching through individual files.

**Data Integrity** - Databases prevent duplicate or inconsistent data through rules and constraints, ensuring your information stays clean and reliable.

**Concurrent Access** - Multiple users or programs can safely read and write data simultaneously without corrupting it.

**Backup and Recovery** - Built-in features to protect against data loss and restore information if something goes wrong.

**Scalability** - Can handle growing amounts of data and users without major restructuring.

---

**List 3 data types that can be used in MySQL and describe them briefly:**

**INT**: Stores whole numbers (integers) like 1, 42, -15, or 1000. Perfect for IDs, counts, ages, or any numeric data without decimals. Range is roughly -2 billion to +2 billion.

**VARCHAR(length)**: Stores text/strings of variable length up to a specified maximum. For example, VARCHAR(50) can hold names, emails, or descriptions up to 50 characters. It only uses the space needed for the actual text stored.

**DATE**: Stores dates in YYYY-MM-DD format like '2024-12-25'. Useful for birthdays, creation dates, deadlines, or any date-related information. MySQL can perform date calculations and comparisons with this type.

---

**In what situations would SQLite be a better choice than MySQL?**

Here are situations where SQLite would be better than MySQL for Python programming:

**Learning and Development**: SQLite requires zero setup or configuration. I can start using it immediately in Python with the built-in `sqlite3` module, while MySQL requires installing and configuring a separate server.

**Small to Medium Applications** - Perfect for personal projects, desktop applications, or web apps with moderate traffic. If I am building a to-do app, personal finance tracker, or small business tool, SQLite handles this easily.

**Portable Applications**: The entire database is just one file that I can copy, move, or backup easily. Great for applications that need to run on different computers or be distributed with my Python program.

**Prototyping and Testing**: Learning or experimenting with database concepts, SQLite lets me focus on SQL and Python code without worrying about server management, user permissions, or network connections.

**Single-User Applications**: If only one person (or one Python process) accesses the database at a time, SQLite is simpler and sufficient.

**Local Data Storage**: When my Python application needs to store data locally on the user's machine rather than on a remote server.

SQLite would be often the best starting point because it removes complexity and lets focus on understanding database concepts and SQL queries.

---

**Think back to what you learned in the Immersion course. What do you think about the differences between JavaScript and Python as programming languages?**

My experience is clearly still limited and I have been learning only the basic concepts of both languages, so my opinion may not be that valuable. However, I have the impression that Python is more direct - its syntax is clearer and its tools are more tailored to its scope.

Python's philosophy of 'there should be one obvious way to do it' really shows, compared to JavaScript's multiple approaches for the same task. The syntax feels more intuitive too - using indentation for code blocks instead of curly braces, and simpler variable declarations like `name = "John"` rather than `let name = "John"`.

What I find particularly impressive about Python are its built-in methods for data manipulation, like list comprehensions that let you transform data in one clean line, or generators that handle memory efficiently. These native features feel naturally integrated into the language, making common programming tasks more straightforward.

Even though I have been working on web projects and I am far more used to JavaScript, I have to admit that I am definitely falling in love with Python, and at this moment, I prefer it.

---

**Now that you’re nearly at the end of Achievement 1, consider what you know about Python so far. What would you say are the limitations of Python as a programming language?**

As I'm still a beginner, I don't have enough experience to fully understand the technical limitations of programming languages yet. However, from what I've learned so far, I can see a few areas where Python might have drawbacks:

**Speed**: Python can be slower than some other languages like C++ or Java for certain tasks. This is because Python prioritizes being easy to read and write over raw performance.

**Mobile Development**: Python isn't commonly used for creating mobile apps. Most mobile apps are built with languages like Swift (iOS), Kotlin/Java (Android), or JavaScript/TypeScript (Universal via React Native).

**Web Frontend**: Frontend has been my main area of expertise till now**,** but while Python is great for backend web development, it is not usable for frontend as JavaScript is the only language a web browser can natively work with.

**Memory Usage**: Python tends to use more memory than some other languages, which could matter for very large applications.

That said, as a beginner, I think Python's advantages - like clear syntax, readability, and extensive libraries - far outweigh these limitations for learning programming fundamentals. Many of these limitations can also be addressed with additional tools or aren't relevant for the types of projects I'm working on right now.

---

---

## Exercise 1.7: Object-Relational Mapping in Python

### Reflection Questions

---

**What is an Object Relational Mapper and what are the advantages of using one?**

An Object Relational Mapper (ORM) is a tool that helps us interact with a database using Python objects instead of writing raw SQL queries. It allows us to work with databases without needing to write pure SQL. Instead, we use Python classes and methods, and the ORM automatically translates our Python code into SQL queries behind the scenes.

An ORM connects Python classes to database tables. We define Python classes to represent our data (e.g., User, Product). Each class maps to a table in the database, and each class attribute (like name, email) maps to a column in that table. The ORM provides methods to create, read, update, and delete (CRUD) records using standard Python code.

**ORM Advantages:**

- Easier to use – Use Python instead of complex SQL.
- Safer – Helps prevent SQL injection attacks.
- Faster development – Less code to write and maintain.
- Portable – Easier to switch databases (e.g., from SQLite to PostgreSQL).
- More readable – Code is often clearer and more Pythonic.

Popular Python ORMs include SQLAlchemy and Django ORM.

---

**By this point, you’ve finished creating your Recipe app. How did it go? What’s something in the app that you did well with? If you were to start over, what’s something about your app that you would change or improve?**

I found the process of creating this app very interesting. I think it has been a good way to get to know Python—at least some of its aspects and features. I believe I did well on the user flow and the UX part. I wouldn't change much; the app is well-structured and well-featured for its purpose, especially as a learning project.

One possible addition could be allowing users to add personal notes to a recipe. However, from a learning point of view, this wouldn’t introduce any new concepts—it would simply involve adding another column to the recipe entry and another option to the main menu.

---

**Imagine you’re at a job interview. You’re asked what experience you have creating an app using Python. Taking your work for this Achievement as an example, draft how you would respond to this question.**

My answer would be as follows:

I have hands-on experience developing a full-featured Recipe Management System using Python, which demonstrates my ability to build practical applications with modern development practices.

The app I created is a comprehensive recipe database application that showcases several key Python development skills. It's built using SQLAlchemy ORM for database management, MySQL as the backend database, and follows object-oriented programming principles with proper class design.

**Key Features I Implemented:**

- Complete CRUD operations (Create, Read, Update, Delete) for recipe management
- Advanced search functionality that allows users to find recipes by ingredients
- Automatic difficulty calculation based on cooking time and ingredient count
- User-friendly command-line interface with comprehensive error handling
- Database schema design with proper relationships and constraints

**Technical Skills Demonstrated:**

- **Database Integration**: Used SQLAlchemy ORM to abstract database operations, making the code more maintainable and secure against SQL injection
- **Environment Management**: Implemented proper configuration management using python-dotenv for database credentials
- **Object-Oriented Design**: Created a Recipe class with methods for data manipulation and business logic
- **Error Handling**: Built robust input validation and exception handling throughout the application
- **User Experience**: Designed an intuitive menu system with confirmation dialogs and clear feedback

**Development Process:**
I followed a progressive development approach, starting with basic file I/O operations and gradually evolving to more complex database-driven functionality. This included working with text files, binary files, and finally implementing a full MySQL database solution with ORM mapping.

The project demonstrates my ability to take a concept from initial planning through to a fully functional application, with attention to both technical implementation and user experience. I'm comfortable working with external libraries, managing dependencies, and following Python best practices for code organization and documentation.

---

**You’ve finished Achievement 1! Before moving on to Achievement 2, take a moment to reflect on your learning in the course so far:**

**What went well during this Achievement?**

As I mentioned in a previous journal entry, my start with Python went very well—I actually "fell in love" with it.

**What’s something you’re proud of?**

It might sound cheesy, but I’m proud of the final result: the entire CLI application. I’ve always found command-line apps fascinating, but I had never built one before. I think they fascinated me because, when I was a kid and saw people in movies using terminal apps, they always looked cool and hacky. :)

**What was the most challenging aspect of this Achievement?**

I encountered many challenging aspects and topics in the previous achievements, but not in this one. Maybe that’s because Python has a very clear and straightforward way of doing things—and because I could rely on the experience I had already gained from using JavaScript.

**Did this Achievement meet your expectations? Did it give you the confidence to start working with your new Python skills? What’s something you want to keep in mind to help you do your best in Achievement 2?**

I didn’t have specific expectations for this Achievement, as I was almost completely new to Python. Still, it definitely met whatever expectations I did have. I think it’s still a bit early to feel fully confident working with Python, but this Achievement has surely been a great starting point.

---

---

## Exercise 2.1: Getting Started with Django

### Reflection Questions

---

**Suppose you’re a web developer in a company and need to decide if you’ll use vanilla (plain) Python for a project, or a framework like Django instead. What are the advantages and drawbacks of each?**

Using plain Python means we build everything from scratch, giving us full control over the project’s structure and logic. This can be a good choice for small, simple applications that don’t require a lot of built-in features, since we avoid the extra weight of a large framework. However, it can be time-consuming to implement common web development tasks—like routing, database handling, and security—on your own, and we’ll need to ensure performance and scalability without the help of a pre-made system.

Using Django, on the other hand, gives us a complete, “batteries-included” framework that’s implemented in Python. It speeds up development with its Model-View-Template (MVT) architecture, follows DRY principles to reduce code repetition, and comes with built-in tools for security, scalability, content delivery, and admin management. This makes it a strong choice for larger, more complex projects that require a backend, database, and robust structure. The trade-offs are that Django enforces its own way of doing things, which can limit flexibility, and it may be overkill for very small or simple applications that don’t need its full set of features.

---

**In your own words, what is the most significant advantage of Model View Template (MVT) architecture over Model View Controller (MVC) architecture?**

The most significant advantage of the Model-View-Template (MVT) architecture over Model-View-Controller (MVC) is mainly in how it simplifies naming and roles in Django. While MVC and MVT work almost the same, Django’s approach shifts the “Controller” responsibilities into what it calls the “View,” and what MVC calls the “View” (the user interface) is instead referred to as a “Template.” This naming matches Django’s workflow more naturally, making it clearer for developers working within the framework. Functionally, the architectures are very similar, the difference lies in terminology and how Django organizes these parts to streamline development.

---

**Now that you’ve had an introduction to the Django framework, write down three goals you have for yourself and your learning process during this Achievement. You can reflect on the following questions if it helps:**

**What do you want to learn about Django?**
Everything I need to start using it confidently in a professional setting.

**What do you want to get out of this Achievement?**
A solid foundational understanding of Django’s core concepts, so I can start off on the right foot and continue building my skills.

**Where or what do you see yourself working on after you complete this Achievement?**
I hope to be able to use Django in an Agentic AI project, where it serves both as the user-facing front end and as the back-end backbone that manages the AI’s operations.
