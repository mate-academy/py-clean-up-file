from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, typ: any, value: any, traceback: any) -> None:
        os.remove(self.filename)
