from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, file_name: str, mode: str = "w") -> None:
        self.filename = file_name
        self.mode = mode

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(
            self,
            exc_type: any,
            exc_value: any,
            exc_traceback: any
    ) -> None:
        self.file.close()
        os.remove(self.filename)
