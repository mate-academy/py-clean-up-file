from __future__ import annotations
import os
from typing import Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: Optional[BaseException],
            exc_val: Optional[BaseException],
            exc_tb: Optional[object]
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
