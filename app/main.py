from __future__ import annotations
from typing import Any
import os


class CleanUpFile:
    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        file_path = f"{os.getcwd()}/{self.filename}"
        if os.path.exists(file_path):
            os.remove(file_path)
