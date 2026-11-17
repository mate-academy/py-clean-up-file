import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> str:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        os.remove(self.filename)
