import os
from typing import Any


class CleanUpFile:

    def __init__(self, filename: Any) -> Any:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        os.remove(self.filename)
