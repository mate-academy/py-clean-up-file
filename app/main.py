import os
from typing import Any


class CleanUpFile:
    """Remove file on exit."""
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        """Nothing to do when entering, just return self"""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Check if the file exists, and remove it if it does"""
        if os.path.exists(self.filename):
            os.remove(self.filename)
