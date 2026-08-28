from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> object:
        self.file = self.filename
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        remove(self.filename)
