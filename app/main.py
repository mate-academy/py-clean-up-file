import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self,
                 exc_type: Any,
                 exc_value: Any,
                 exc_traceback: Any) -> None:
        self.file.close()

    def __del__(self) -> None:
        os.remove(self.filename)
