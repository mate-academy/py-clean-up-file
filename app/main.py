import os
from typing import Optional, Type, Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[Any]
    ) -> Optional[bool]:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return None
