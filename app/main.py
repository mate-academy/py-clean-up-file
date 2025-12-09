import os
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.mode = "w"
        self.file = None

    def __enter__(self) -> object:
        self.file = open(self.filename, self.mode)
        return self

    def write(self, data: str) -> int:
        return self.file.write(data)

    def __exit__(
            self,
            exc_type: type | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> None:
        if self.file:
            self.file.close()
            try:
                os.remove(self.filename)
            except FileNotFoundError:
                pass
        self.file = None
