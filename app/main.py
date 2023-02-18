from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str, method: str = "w") -> None:
        self.filename = filename
        self.file_obj = open(self.filename, method)

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.file_obj.close()
        os.remove(self.filename)
