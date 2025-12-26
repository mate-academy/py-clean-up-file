import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        open(self.filename, "w").close()
        return self

    def __exit__(self, exc_type: str, exc_value: int, traceback: str) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
