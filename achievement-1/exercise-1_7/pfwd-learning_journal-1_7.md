# Python for Web Developers Learning Journal

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
