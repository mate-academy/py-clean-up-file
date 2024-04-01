from os import remove
from typing import Any


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.file_object = None
        self.filename = filename

    def __enter__(self) -> object:
        try:
            self.file_object = open(self.filename, "w")
        finally:
            return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.file_object.close()
        remove(self.filename)
