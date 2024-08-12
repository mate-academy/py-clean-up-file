import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        pass

    def __enter__(self) -> Any:
        return self

    def __exit__(
            self,
            ecx_type: str,
            exc_value: str,
            exc_traceback: str
    ) -> Any:
        if os.path.isfile(self.filename):
            os.remove(self.filename)
        return False
