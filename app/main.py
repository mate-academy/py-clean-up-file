import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        self.file = open(self.filename, "w")
        return self.filename

    def __exit__(self, exc_type: type, exc_val: str,
                 exc_tb: BaseException) -> None:
        self.file.close()
        os.remove(self.filename)
