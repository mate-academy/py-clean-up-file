from __future__ import annotations
from os import remove as os_remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: type,
            exc_val: BaseException,
            exc_tb: object
    ) -> None:
        try:
            os_remove(self.filename)
        except (FileNotFoundError, FileExistsError):
            return
