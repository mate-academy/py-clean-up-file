import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_obj = open(filename, "w")

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any,
                 exc_val: Any,
                 exc_tb: Any) -> None:
        self.file_obj.close()
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
