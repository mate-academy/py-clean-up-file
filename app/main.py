import os


class CleanUpFile:
    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: str, exc_val: int, exc_tb: str) -> None:
        self.file.close()
        os.remove(self.filename)
