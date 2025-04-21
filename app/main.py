import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> object:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: None, exc_va: None, exc_tb: None) -> None:
        self.file.close()
        os.remove(f"{self.filename}")
