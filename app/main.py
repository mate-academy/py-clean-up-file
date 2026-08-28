import os


class CleanUpFile:
    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self, exc_type: bool, exc_value: bool, traceback: bool
    ) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return False
