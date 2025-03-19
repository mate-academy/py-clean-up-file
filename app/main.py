import os
from typing import Optional, Type
import traceback


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> str:
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[traceback]) -> None:
        os.remove(self.filename)
    # write your code here
    pass
