import os


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        with open(self.filename, "w") as file:
            file.write("Hello Mate!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.filename)
