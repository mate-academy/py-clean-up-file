import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = open(self.filename, "w+")

    def __enter__(self) -> type:
        return self

    def __exit__(self, *args: tuple) -> None:
        self.file.close()
        os.remove(self.filename)
