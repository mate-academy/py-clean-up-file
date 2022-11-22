import os


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type: type,
                 exc_val: str,
                 exc_tb: str) -> None:

        os.remove(self.filename)
