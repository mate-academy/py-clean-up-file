import os
from typing import Type
from types import TracebackType


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":

        return self

    def __exit__(
            self,
            exc_type: Type[Exception] | None,
            exc_value: Exception | None,
            exc_traceback: TracebackType | None,
    ) -> None:

        if os.path.exists(self.filename):
            os.remove(self.filename)
