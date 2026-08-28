from os import remove
from types import TracebackType
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> None:
        if self.file is not None:
            self.file.close()
        try:
            remove(self.filename)
        except OSError as e:
            print(f"Error deleting the file: {e}")
