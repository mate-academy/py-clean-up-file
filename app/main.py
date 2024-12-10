import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: BaseException,
                 exc_val: BaseException, exc_tb: Exception) -> None:
        os.remove(self.filename)
