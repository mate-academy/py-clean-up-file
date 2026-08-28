import os
from typing import Optional, Type
from types import TracebackType


class CleanUpFile:
    """
    Контекстний менеджер, який видаляє файл після виходу з блоку with.
    """

    def __init__(self, filename: str) -> None:
        """
        Ініціалізує контекстний менеджер з ім'ям файлу.

        Args:
            filename (str): Ім'я файлу, який потрібно видалити.
        """
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        """
        Входить в контекстний менеджер.
        """
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> Optional[bool]:
        """
        Виходить з контекстного менеджера та видаляє файл, якщо він існує.

        Args:
            exc_type: Тип винятку, якщо він виник.
            exc_value: Значення винятку, якщо він виник.
            traceback: Traceback винятку, якщо він виник.
        """
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"Файл '{self.filename}' видалено.")
        else:
            print(f"Файл '{self.filename}' "
                  f"не існує, тому видалення не потрібне.")
        return None
