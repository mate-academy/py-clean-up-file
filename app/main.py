import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.file = open(filename, "w")
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self, typ: Any, value: Any, traceback: Any) -> None:
        self.file.close()
        os.remove(self.filename)
