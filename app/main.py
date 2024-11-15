from typing import Optional, Type
from types import TracebackType
import os


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File '{self.filename}' has been removed.")
