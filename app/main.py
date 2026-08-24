import os
from types import TracebackType


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename: str = file_name

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
