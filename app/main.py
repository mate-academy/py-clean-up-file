import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: Any) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self,
                 exc_type: Any = None,
                 exc_val: Any = None,
                 exc_tb: Any = None) -> None:
        os.remove(self.filename)
