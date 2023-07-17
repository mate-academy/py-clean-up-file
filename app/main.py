from __future__ import annotations
from types import TracebackType
from typing import Type
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self,
                 exc_type: Type[BaseException] | None,
                 exc_val: BaseException | None,
                 exc_traceback: TracebackType | None) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        else:
            print("File is not present in the system.")
