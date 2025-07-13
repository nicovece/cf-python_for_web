# Python for Web Developers Learning Journal

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
