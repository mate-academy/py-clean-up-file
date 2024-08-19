from __future__ import annotations
from typing import Optional, Type
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[Type[BaseException]]) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
