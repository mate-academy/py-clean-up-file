import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: str, exc_value: int, traceback: str) -> None:
        self.file.close()
        os.remove(f"{self.filename}")
