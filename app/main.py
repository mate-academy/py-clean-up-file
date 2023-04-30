import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, typ: object, value: int, traceback: int) -> None:
        os.remove(self.filename)
