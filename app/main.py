import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> None:
        self.file = open(self.filename, "w+")
        return self

    def __exit__(self, exc_type: str, exc_value: str, traceback: str) -> None:
        self.file.close()
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
