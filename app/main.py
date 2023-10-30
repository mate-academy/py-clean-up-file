from __future__ import annotations
from types import TracebackType
from typing import Optional, Type
from os import remove, path


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        if path.exists(self.file_name):
            remove(self.file_name)
