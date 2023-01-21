import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def __del__(self):
        os.remove(self.filename)
