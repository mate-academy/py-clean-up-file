import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> None:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        self.file.close()
        os.remove(self.filename)
