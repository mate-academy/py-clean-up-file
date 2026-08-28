import os


class CleanUpFile:
    def __init__(self, filename: str, open_type: str = "w") -> None:
        self.filename = filename
        self.open_type = open_type
        self.file = None

    def __enter__(self) -> any:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: str, exc_value: str, traceback: str) -> None:
        if self.file:
            self.file.close()

        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
