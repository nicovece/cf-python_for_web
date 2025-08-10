# Python for Web Developers Learning Journal

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
