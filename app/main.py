import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    pass
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if os.path.exists(self.filename):
            os.remove(self.filename)
