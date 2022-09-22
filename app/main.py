from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, file_name) -> None:
        self.filename = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        os.remove(self.filename)
