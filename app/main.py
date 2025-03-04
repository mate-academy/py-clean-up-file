from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

        file_len = filename.split()
        if len(file_len) > 1:
            return

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: None,
                 exc_value: None, traceback: None) -> None:
        pass

    def __del__(self) -> None:
        os.remove(self.filename)
