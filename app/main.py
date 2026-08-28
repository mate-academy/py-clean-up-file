import os
from types import TracebackType
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc: Optional[BaseException],
            traceback: Optional[TracebackType]
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
