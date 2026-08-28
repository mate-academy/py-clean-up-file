import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> None:
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self, exc_type: type,
            exc_value: type,
            exc_traceback: type) -> None:
        if self.file:
            self.file.close()
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            print(f"File {self.filename} not found for deletion.")
        return False
