import os
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.file: Optional[open] = None

    def __enter__(self) -> "CleanUpFile":
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()

        self.file = open(self.filename, "r")
        return self

    def read(self) -> str:
        if self.file:
            return self.file.read()
        return ""

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[object]
    ) -> None:
        if self.file:
            self.file.close()

    def __del__(self) -> None:
        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
        except Exception:
            pass
