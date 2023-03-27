from __future__ import annotations
import os
from typing import Union
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: Union[type, None],
            exc_val: Union[Exception, None],
            exc_tb: Union[TracebackType, None]
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
