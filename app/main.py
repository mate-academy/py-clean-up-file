import os
from types import TracebackType
from typing import Optional, Type


class CleanUpFile:
    """Context manager that removes the specified file on exit."""

    def __init__(self, filename: str) -> None:
        """Initialize with the filename to clean up."""
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        """Enter the runtime context related to this object."""
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:
        """Remove the file if it exists when exiting the context."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
        # Do not suppress exceptions
        return False


