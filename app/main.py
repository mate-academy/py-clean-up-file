import os
from typing import Any


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self, mode: str = "w") -> Any:
        self.file = open(self.filename, mode)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.file.close()
        os.remove(self.filename)
