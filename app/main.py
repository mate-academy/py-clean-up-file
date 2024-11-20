from os import remove, path
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.mode = "w"
        self.file = None

    def __enter__(self) -> Any:
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.file.close()
        if self.file is not None:
            remove(path.abspath(self.filename))
