import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.f = None

    def __enter__(self) -> None:
        self.f = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: int, exc_val: int, exc_tb: int) -> None:
        self.f.close()
        os.remove(self.filename)
