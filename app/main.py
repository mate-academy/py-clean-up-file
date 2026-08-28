import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        self.file = open(f"{self.filename}", "w")
        return self

    def __exit__(
            self,
            exc_type: type,
            exc_val: Exception,
            exc_tb: Any
    ) -> None:
        self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
