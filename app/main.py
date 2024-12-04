import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(
            self,
            exc_type: object = None,
            exc_val: object = None,
            exc_tb: str = None
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


CleanUpFile("file.txt")
