import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        try:
            os.remove(self.filename)
        except OSError:
            print(f"File {self.filename} doesn't exist.")
