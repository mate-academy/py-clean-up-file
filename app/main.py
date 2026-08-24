from os import remove, path
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: type | None,
            exc_value: BaseException | None,
            traceback: TracebackType | None) -> None:
        if path.exists(self.filename):
            remove(self.filename)
