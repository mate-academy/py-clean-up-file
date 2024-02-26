import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Exception, exc_val: Any, exc_tb: Any) -> Any:
        os.remove(os.path.abspath(f"{self.filename}"))
