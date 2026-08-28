from __future__ import annotations
from typing import Optional, Type
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        pass

    def __enter__(self) -> CleanUpFile:
        with open(self.filename, "w") as file:
            file.write("hello world")
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[object]
    ) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
