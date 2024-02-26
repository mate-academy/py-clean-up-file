import os
from typing import Optional, Type, Any, Union


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[Union[Type[BaseException], Any]],
    ) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
