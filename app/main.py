import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> Any:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        if os.path.exists(self.filename):
            if isinstance(self.filename, str):
                os.remove(self.filename)
