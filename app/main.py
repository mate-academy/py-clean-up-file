import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> Any:
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type: Any, exc_value: Any, exc_traceback: Any)\
            -> None:
        self.file.close()
        os.remove(self.filename)
