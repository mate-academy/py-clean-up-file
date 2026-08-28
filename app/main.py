import os
from typing import Any


class CleanUpFile(object):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, mode: Any, value: Any, traceback: Any) -> None:
        os.remove(self.filename)
