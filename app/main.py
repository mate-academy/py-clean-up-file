from types import TracebackType
from typing import Optional, Type, Any
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc: Optional[BaseException],
            traceback: Optional[TracebackType]
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
