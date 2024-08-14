import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        try:
            open(self.filename, "r+")
        except FileNotFoundError:
            print(f"File {self.filename} not found")
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        if os.path.isfile(self.filename):
            os.remove(self.filename)
