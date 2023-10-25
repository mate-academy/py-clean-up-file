from __future__ import annotations
import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: type, exc_val: str, exc_tb: str) -> None:
        pass

    def __del__(self) -> None:
        try:
            os.remove(self.filename)
        except Exception:
            pass
