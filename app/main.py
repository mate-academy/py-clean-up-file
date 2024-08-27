from typing import Any
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Exception,
                 exc_value: Exception,
                 exc_traceback: Exception) -> Any:
        if os.path.exists(self.filename):
            os.remove(self.filename)
