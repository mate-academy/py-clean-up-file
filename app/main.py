from os import remove


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        remove(self.filename)
