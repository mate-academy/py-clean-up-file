import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> object:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: any, exc_val: any, exc_tb: any) -> None:
        self.file.close()

    def __del__(self) -> None:
        os.remove(self.filename)
