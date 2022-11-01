import os
from typing import Any


class CleanUpFile:
    def __init__(
            self,
            file_name: str,
            mode: str = "r"
    ) -> None:
        self.filename = file_name
        self.mode = mode

    def __enter__(self) -> Any:
        return self

    def __exit__(
            self,
            exc_type: Any,
            exc_val: Any,
            exc_tb: Any
    ) -> None:
        path = os.path.join(self.filename)
        os.remove(path)
