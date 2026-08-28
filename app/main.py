from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: str, ex_val: str, ex_traceback: str) -> None:
        try:
            os.remove(self.filename)
        except Exception:
            pass
