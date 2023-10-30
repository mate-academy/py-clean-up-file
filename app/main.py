import os
from typing import Optional, Type, Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_obj = None

    def __enter__(self) -> "CleanUpFile":
        self.file_obj = open(self.filename, "w")
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[Type[BaseException] | Any]
    ) -> None:
        if self.file_obj:
            self.file_obj.close()

        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
        except FileNotFoundError:
            pass
