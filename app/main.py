from __future__ import annotations
from typing import Any
import os


class CleanUpFile:

    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self,
                 exc_type: Any,
                 exc_val: Any,
                 exc_tb: Any) -> None:

        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
