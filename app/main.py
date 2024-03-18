import os
import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> object:
        return self

    def __exit__(self,
                 exc_type: Any,
                 exc_value: Any,
                 traceback: Any) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
