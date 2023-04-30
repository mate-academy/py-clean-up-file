import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, ype: object, value: int, traceback: int) -> None:
        os.remove(self.filename)
