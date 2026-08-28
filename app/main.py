import os
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exec_type: type[BaseException] | None,
                 exec_val: BaseException | None,
                 exec_tb: TracebackType | None) -> None:
        os.remove(self.filename)
