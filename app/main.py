import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> callable:
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return False
