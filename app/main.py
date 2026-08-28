import os


class CleanUpFile:

    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> isinstance:
        return self

    def __exit__(self, *args) -> None:
        os.remove(self.filename)
