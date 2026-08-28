import os
from types import TracebackType
from typing import Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        print("entered")
        return self

    def __exit__(self, exc_type: Type[BaseException],
                 exc_val: BaseException,
                 exc_tb: TracebackType) -> None:
        os.remove(self.filename)
