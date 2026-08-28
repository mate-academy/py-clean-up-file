import os


class CleanUpFile:
    def __init__(self, filename, mode="w") -> None:
        self.filename = filename
        self.mode = mode
        self.file = self.file = open(self.filename, self.mode)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        os.remove(self.filename)
