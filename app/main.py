import os
from typing import Optional, Self, Type
from types import TracebackType


class CleanUpFile(object):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Self:
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
