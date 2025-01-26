import os


class CleanUpFile:
    def __init__(self, filename) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        os.remove(self.filename)
        return True
