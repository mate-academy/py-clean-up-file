from typing import TextIO
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> TextIO:
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self,
            exc_type: Exception,
            exc_val: Exception,
            exc_tb: Exception
    ) -> None:
        self.file.close()
        return os.remove(self.filename)
