from __future__ import annotations
from typing import Optional, Type, Tuple
from os import remove


class CleanUpFile:
    def __init__(self, filename : str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[Tuple]
    ) -> None:
        if self.file:
            self.file.close()
        remove(self.filename)
