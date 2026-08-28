import os
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.mode = "w"
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if self.file:
            self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
