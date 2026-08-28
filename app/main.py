from types import TracebackType
from typing import Type, Optional
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = self

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self, exc_type: Optional[Type[BaseException]],
            exc: Optional[BaseException],
            traceback: Optional[TracebackType]
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
