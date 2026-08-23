import os
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None
        self.mode = "w"

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(
            self,
            exc_type: type | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None,
    ) -> None:
        self.file.close()
        os.remove(self.filename)
