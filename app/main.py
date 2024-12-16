from __future__ import annotations

from os import path, remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: object | None,
            exc_val: object | None,
            exc_tb: object | None
    ) -> bool:
        if path.exists(self.filename):
            remove(self.filename)
        return False
