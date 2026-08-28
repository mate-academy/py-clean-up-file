from __future__ import annotations
import os
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: BaseException | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> None:
        files_in_dir = os.listdir(".")

        if self.filename in files_in_dir:
            os.remove(self.filename)
