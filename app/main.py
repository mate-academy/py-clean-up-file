import os
from types import TracebackType
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename

    def __enter__(self) -> "CleanUpFile":
        """Called when entering the 'with' block."""
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        """Called when exiting the 'with' block, regardless of exceptions."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
