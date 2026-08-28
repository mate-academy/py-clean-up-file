import os
from typing import Optional, Type
import types


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w", encoding="utf-8")
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[types.TracebackType]
    ) -> Optional[bool]:
        if self.file and not self.file.closed:
            self.file.close()

        if os.path.exists(self.filename):
            os.remove(self.filename)
        return None
