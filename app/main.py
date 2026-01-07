import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        self.file = open(self.filename, "r")
        return self

    def __exit__(self, *args) -> None:
        self.file.close()
        os.remove(self.filename)
