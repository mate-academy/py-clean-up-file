import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: type, exc_value: int, traceback: str) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
