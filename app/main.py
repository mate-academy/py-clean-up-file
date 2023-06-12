import os
from types import TracebackType as Traceback


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: TypeError,
            exc_val: ValueError,
            exc_tb: Traceback
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
