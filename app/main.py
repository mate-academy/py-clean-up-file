from os.path import exists
from os import remove


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exists(self.filename):
            remove(self.filename)
