from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_name = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> bool:
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        return False
