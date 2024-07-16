from __future__ import annotations

import os


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        os.remove(self.filename)
