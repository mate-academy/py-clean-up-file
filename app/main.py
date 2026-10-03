import os
from types import TracebackType
from typing import IO, Optional, Type


class CleanUpFile:

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.file: Optional[IO[str]] = None

    def __enter__(self) -> IO[str]:
        self.file = open(self.file_name, "r", encoding="utf-8")
        return self.file

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        if self.file and not self.file.closed:
            self.file.close()

        if os.path.exists(self.file_name):
            os.remove(self.file_name)
