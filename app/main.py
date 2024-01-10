import os
from typing import Any


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: Any,
                 exc_val: type,
                 exc_tb: str) -> None:
        pass

    def __del__(self) -> None:
        os.remove(self.filename)
