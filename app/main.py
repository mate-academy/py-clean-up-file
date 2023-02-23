from __future__ import annotations
import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_obj = None

    def __enter__(self) -> CleanUpFile:
        self.file_obj = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.file_obj.close()
        os.remove(self.filename)
