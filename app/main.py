import os
from inspect import Traceback
from typing import Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: Optional[type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[Traceback]) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        else:
            print(f"{self.filename} is not exist.")
