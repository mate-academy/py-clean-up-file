# Сlean Up File

**Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

Create a custom context manager:

In this task, create a custom context manager.
Implement the `CleanUpFile` context manager as a class. It should remove the file if it exists after exiting.

Its `__init__` method should accept only the filename parameter. 
Also, `CleanUpFile` must have **enter** and **exit** methods.

For example:
```python
with CleanUpFile(“file.txt”):
    with open(“file.txt”, “w”) as file:
        file.write(“Hello Mate!”)
```

After executing the code, the "file.txt" file should not exist.
