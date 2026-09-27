import os
from types import TracebackType
from typing import Self


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: type, exc_value: BaseException,
                 traceback: TracebackType) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
