from __future__ import annotations
import os
from typing import Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: Type[BaseException] | None,
            exc_tb: str
    ) -> None:
        os.remove(self.filename)
