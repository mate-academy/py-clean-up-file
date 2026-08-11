import os

from typing import Optional, Type

from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        with open(self.filename, "w") as f:
            f.write(self.filename)
            return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
    ) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
