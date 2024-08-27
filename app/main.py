import os
from typing import Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: Optional[object],
            exc_value: Optional[object],
            traceback: Optional[object]
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return False
