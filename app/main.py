import os
import types
from typing import Self


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Self:
        print(f"Entering context: {self.filename}")
        return self

    def __exit__(self,
                 exc_type: type[BaseException] | None,
                 exc_val: BaseException | None,
                 exc_tb: types.TracebackType | None) -> bool:
        print(f"Exiting context: {self.filename}")

        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"✓ File deleted: {self.filename}")

        return False
