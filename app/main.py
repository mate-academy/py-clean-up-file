import os

from typing import Any


class CleanUpFile:
    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        os.remove(self.filename)
