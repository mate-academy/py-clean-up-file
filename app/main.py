import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = open(self.filename, "w")

    def __enter__(self) -> None:
        return self

    def __exit__(
            self,
            exc_type: object,
            exc_val: object,
            exc_tb: object
    ) -> None:
        os.remove(self.filename)
