import os
from typing import Self


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Self:
        return self

    def __exit__(
            self,
            exc_type: type | None,
            exc_val: Exception | None,
            exc_tb: object
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
