import os


class CleanUpFile:
    def __init__(self, filepath: str) -> None:
        self.filename = filepath

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        os.remove(self.filename)
