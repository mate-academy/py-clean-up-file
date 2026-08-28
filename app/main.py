from __future__ import annotations
from typing import Any
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self,
                 file_type: type,
                 value: Any,
                 traceback: Exception) -> None:

        os.remove(self.filename)
