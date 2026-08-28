from __future__ import annotations
from typing import Type
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: Type[BaseException],
            exc_val: BaseException,
            exc_tb: Type
    ) -> None:
        open(self.filename, "r")
        os.remove(self.filename)
