from __future__ import annotations
from typing import Any
import os


class CleanUpFile:
    def __init__(self, filename: str, mode: str = "w") -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self,
                 exc_type: type[BaseException] | None,
                 exc_val: BaseException | None,
                 exc_tb: Any | None,
                 ) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return False
