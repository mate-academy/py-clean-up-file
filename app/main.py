import os


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def __del__(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)
