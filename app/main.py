import os


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"file '{self.filename}' was deleted.")
        else:
            print(f"file '{self.filename}' was not found.")
