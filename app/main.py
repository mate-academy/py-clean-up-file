import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> any:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> any:
        self.file.close()
        os.remove(self.filename)
