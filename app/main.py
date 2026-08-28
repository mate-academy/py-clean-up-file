from __future__ import annotations
import os.path


class CleanUpFile:
    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
        self,
        exc_type: BaseException,
        exc_val: BaseException,
        exc_tb: object,
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
