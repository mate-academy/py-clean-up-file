import os

class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        # Return self to allow for additional operations in the context if needed
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Remove the file if it exists
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File {self.filename} has been removed.")

# Example usage:
with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")

# After exiting the context, the file "file.txt" will be removed.
