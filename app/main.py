import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "a")
        return self

    def __exit__(self, exc_type: str, exc_value: str, traceback: str) -> bool:
        self.file.close()
        os.remove(self.filename)
        return False
