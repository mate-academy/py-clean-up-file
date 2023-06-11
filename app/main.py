import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        os.remove(self.filename)
