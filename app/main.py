import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.f = None

    def __enter__(self) -> object:
        self.f = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        self.f.close()
        os.remove(self.filename)
