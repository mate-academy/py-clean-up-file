import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        """Initialize context manager with the file name."""
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        """Enter the runtime context."""
        # Nothing special to do before entering
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Exit the runtime context and remove the file if it exists."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
