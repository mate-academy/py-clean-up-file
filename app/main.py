import os
from typing import Any, Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(
        self, 
        exc_type: Optional[Type[BaseException]], 
        exc_value: Optional[BaseException], 
        traceback: Optional[Any]
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
