import os.path
from os import remove
from typing import Optional, Type
from types import TracebackType



class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            exc_traceback: Optional[TracebackType],
    ) -> None:
        if os.path.exists(self.filename):
            remove(self.filename)
