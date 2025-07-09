import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self) -> None:
        self.file.close()
        if self.file:
            os.remove(self.filename)
