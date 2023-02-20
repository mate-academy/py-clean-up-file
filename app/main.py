from __future__ import annotations
from types import TracebackType

import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exception_type: BaseException | None,
            exception_value: BaseException | None,
            traceback: TracebackType
    ) -> None:
        os.remove(self.filename)
