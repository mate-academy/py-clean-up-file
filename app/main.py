import os
from typing import Any


class CleanUpFile:
    def __init__(
            self,
            file_name: str,
    ) -> None:
        self.filename = file_name

    def __enter__(self) -> object:
        return self

    def __exit__(
            self,
            tp: Any,
            value: Any,
            traceback: Any
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
