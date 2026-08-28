import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> str:
        try:
            self.file = open(self.filename)
            return self.file
        except FileNotFoundError:
            return self

    def __exit__(self, exc_type: str,
                 exc_value: str,
                 exc_traceback: str) -> None:
        try:
            self.file.close()
            os.remove(self.filename)
        except AttributeError:
            os.remove(self.filename)
