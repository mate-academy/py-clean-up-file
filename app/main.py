from typing import Any
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self,
                 exc_type: Any,
                 exc_val: Any,
                 exc_tb: Any) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
