import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> None:
        self.file = open(self.filename)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
