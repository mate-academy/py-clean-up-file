import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> str:
        return self

    def __exit__(self, exc_type: str, exc_value: str, traceback: str) -> None:
        # Remove the file if it exists
        if os.path.exists(self.filename):
            os.remove(self.filename)
