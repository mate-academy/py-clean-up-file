import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self, mode: str = "w") -> "CleanUpFile":
        try:
            self.file = open(self.filename, mode)
        except FileNotFoundError:
            self.file = None
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        if self.file:
            self.file.close()
            os.remove(self.filename)
