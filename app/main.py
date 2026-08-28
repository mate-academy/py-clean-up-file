import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_obj = open(self.filename, "w")

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: object, exc_val: os, exc_tb: object) -> None:
        self.file_obj.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
