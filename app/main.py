import os
from typing import Optional, Type
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> None:
        try:
            remove_file = open(self.filename, "r")
            remove_file.close()
            os.remove(self.filename)
        except FileNotFoundError:
            pass
