import os


class CleanUpFile(object):

    def __init__(self, file_name: str) -> None:
        self.filename = file_name
        self.file = None

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        os.remove(self.filename)
