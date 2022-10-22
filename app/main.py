import os
from typing import TextIO


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> TextIO:
        self.file = open(self.filename)
        return self.file

    def __exit__(self, typo: str, value: str, traceback: str) -> None:
        self.file.close()
        os.remove(self.filename)
