from __future__ import annotations

import os


class CleanUpFile:
    def __init__(self, filename: str, mode: str = "r") -> None:
        self.filename, self.mode = filename, mode
        self.file = None

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self, exc_type: str,
            exc_value: str, exc_traceback: str
    ) -> None:
        os.remove(self.filename)
