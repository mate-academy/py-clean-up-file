import os
from types import TracebackType
from typing import Optional, Type


class CleanUpFile:
    def __init__(self: "CleanUpFile", filename: str) -> None:
        self.filename = filename

    def __enter__(self: "CleanUpFile") -> "CleanUpFile":
        return self

    def __exit__(
        self: "CleanUpFile",
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
