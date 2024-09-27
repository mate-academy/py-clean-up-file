import os
from typing import Any


class CleanUpFile:
    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self,
                 exc_type: Any,
                 exc_value: Any,
                 exc_traceback: Any) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
