import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        try:
            with open(self.filename, "r"):
                os.remove(self.filename)
        except FileNotFoundError:
            pass
