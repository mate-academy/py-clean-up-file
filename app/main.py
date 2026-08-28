import os
from typing import Optional, Type


class CleanUpFile:
    """Context manager that removes the given file on exit."""

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> str:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[object],
    ) -> bool:
        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
        except FileNotFoundError:
            # If already gone, ignore
            pass
        # Do not suppress exceptions from the with-block
        return False
