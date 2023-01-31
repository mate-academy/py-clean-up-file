from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = open(filename, "w")

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, *args) -> None:
        self.file.close()
        self.__del__()

    def __del__(self) -> None:
        if os.path.isfile(self.filename):
            os.remove(self.filename)
