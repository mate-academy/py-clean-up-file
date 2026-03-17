from __future__ import annotations
from types import TracebackType
import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: type | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> None:
        os.remove(self.filename)
