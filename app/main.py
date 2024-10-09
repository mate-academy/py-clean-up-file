from __future__ import annotations

import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: # noqa 001
        self.file.close()
        if os.path.isfile(self.filename):
            self.__del__()

    def __del__(self) -> None:
        os.remove(self.filename)
