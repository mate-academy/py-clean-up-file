import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, *args) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
