from typing import Callable
import os


class CleanUpFile:
    def __init__(self, filename: str, mode: str = "w") -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> object:
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(
            self,
            exc_type: Exception,
            exc_val: Exception,
            exc_tb: Callable
    ) -> None:
        self.file.close()
        os.remove(self.filename)
