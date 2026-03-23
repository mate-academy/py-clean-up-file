import os
from types import TracebackType
from typing import Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        # Нічого не робимо
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        # Видалення файлу, якщо він є
        if os.path.exists(self.filename):
            os.remove(self.filename)
