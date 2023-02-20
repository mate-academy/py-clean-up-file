import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: object, exc_val: os, exc_tb: object) -> None:
        if os.path.isfile(self.filename):
            os.remove(self.filename)
