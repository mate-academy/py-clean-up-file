import os


class CleanUpFile:
    def __init__(self, filename: str, mode: str = "r"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.filename)
    pass
