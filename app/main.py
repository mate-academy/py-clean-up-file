import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        self.file.close()
        os.remove(self.filename)
