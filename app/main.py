from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: type | None,
            exc_val: BaseException | None,
            exc_tb: type | None) -> CleanUpFile:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return self


with CleanUpFile("file.txt") as f:
    pass
