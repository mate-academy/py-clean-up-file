import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self,
            exc_type: object,
            exc_val: object,
            exc_tb: object) -> None:
        if self.file:
            self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
