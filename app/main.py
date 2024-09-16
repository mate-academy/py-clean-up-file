import os


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()
        os.remove(self.filename)
