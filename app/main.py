from __future__ import annotations

import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename)
        return self

    def __exit__(self, exc_type: type, exc_val: str, exc_tb: str) -> None:
        self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
