from __future__ import annotations
from os import remove, path
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self,
                 exception_type: Optional[Type[BaseException]],
                 exception_value: Optional[BaseException],
                 traceback: Optional[Type[BaseException]]
                 ) -> None:
        if path.exists(self.filename):
            remove(self.filename)
