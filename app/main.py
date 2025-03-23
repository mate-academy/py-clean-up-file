from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: type[BaseException],
            exc_value: BaseException,
            traceback: type[BaseException]
    ) -> None:
        os.remove("file.txt")

    def __del__(self) -> None:
        pass
