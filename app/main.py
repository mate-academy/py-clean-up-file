import os
from typing import Self


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args) -> None:
        if os.path.isfile(self.filename):
            os.remove(self.filename)
