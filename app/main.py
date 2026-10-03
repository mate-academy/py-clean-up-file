import os
from types import TracebackType
from typing import IO, Optional, Type


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file: Optional[IO[str]] = None

    def __enter__(self) -> IO[str]:
        if not self.file and not self.file.closed:
            self.file = open(self.filename, "r", encoding="utf-8")
        return self.file

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        if self.file and not self.file.closed:
            self.file.close()

        if os.path.exists(self.filename):
            os.remove(self.filename)
