import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file.read()

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.file.close()
        os.remove(self.filename)
