import os
from typing import Optional, Any, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> object:
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()

        self.file = open(self.filename)
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[Any]) -> None:
        if self.file:
            self.file.close()

        if os.path.exists(self.filename):
            os.remove(self.filename)
