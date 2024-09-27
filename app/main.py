from os import remove


class CleanUpFile:
    def __init__(self, filename, mode="w"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()
        remove(self.filename)
