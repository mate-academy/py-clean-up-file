from __future__ import annotations
import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, type_exc: str, value: str, traceback: str) -> None:
        os.remove(self.filename)
