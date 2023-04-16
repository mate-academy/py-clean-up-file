import os
from typing import Any


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> Any:
        return self

    def __exit__(self,
                 exc_type: Any = None,
                 exc_val: Any = None,
                 exc_tb: Any = None) -> None:
        os.remove(self.filename)
