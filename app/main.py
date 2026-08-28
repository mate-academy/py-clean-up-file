import os
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> None:
        self.file = open(self.filename, "a+")
        return self

    def __exit__(
            self,
            exc_type: type[BaseException] | None,
            exc_value: BaseException | None,
            traceback: TracebackType | None
    ) -> None:
        if self.file:
            self.file.close()

        if os.path.exists(self.filename):
            os.remove(self.filename)
