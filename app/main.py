import os
from typing import Self, Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[object]
    ) -> None:
        pass

    def __del__(self) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
