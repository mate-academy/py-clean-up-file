from __future__ import annotations

import os
from typing import Optional, Type


class CleanUpFile:
    def __init__(self,
                 filename: str
                 ) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self,
                 exception_type: Optional[Type[BaseException]],
                 exception_value: Optional[BaseException],
                 traceback: Optional[Type[BaseException]]
                 ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
