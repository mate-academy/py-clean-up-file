import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_object = open(f"{self.filename}", "w")

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: type, exc_val: str, exc_tb: str) -> None:
        self.file_object.close()
        os.remove(f"{self.filename}")
