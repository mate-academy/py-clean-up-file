import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback) -> bool | None:
        os.remove(self.filename)
