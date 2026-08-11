import os
from types import TracebackType
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"Plik '{self.filename}' został usunięty.")
        else:
            msg = (
                f"Plik '{self.filename}' nie został znaleziony, "
                "więc nie został usunięty."
            )
            print(msg)
