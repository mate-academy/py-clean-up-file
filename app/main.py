from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: Exception | None,
                 exc_value: Exception | None,
                 exc_traceback: Exception | None) -> bool:
        if not self.filename:
            return False
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return True
