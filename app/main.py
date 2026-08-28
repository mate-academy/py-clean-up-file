from __future__ import annotations
import os
import pathlib


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        self.file = open(f"{self.filename}", "w")
        return self

    def __exit__(
            self,
            exc_type: object = None,
            exc_value: object = None,
            exc_traceback: object = None
    ) -> None:
        self.path = pathlib.Path(f"{self.filename}")
        try:
            self.file.close()
            os.remove(self.path)
        except FileNotFoundError:
            pass
