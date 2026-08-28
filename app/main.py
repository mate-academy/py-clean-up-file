import os
from typing import Optional, Type, Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[Any]
    ) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
        except (OSError, IOError):
            print(f"Failed to delete file: {self.filename}")
