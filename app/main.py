from __future__ import annotations
from os import remove, path


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self,
                 exc_type: ValueError | TypeError,
                 exc_val: str | None,
                 exc_tb: bool) -> None:
        if hasattr(self, "file"):
            self.file.close()
        if path.exists(self.filename):
            remove(self.filename)
