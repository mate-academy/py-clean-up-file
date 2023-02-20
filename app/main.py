import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self, type_ex: Any, value_ex: Any, traceback: Any) -> None:
        os.remove(self.filename)
