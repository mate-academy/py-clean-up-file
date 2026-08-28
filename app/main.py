import os
from typing import Optional, TextIO, Any


class CleanUpFile:
    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file: Optional[TextIO] = None

    def __enter__(self) -> "CleanUpFile":  # Стрічкова анотація для типу
        try:
            self.file = open(self.filename, "r")
            return self  # Повертаємо сам екземпляр класу
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
            self.file = None
            return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        # Перевіряємо, чи файл був відкритий
        if self.file:
            try:
                self.file.close()
            except Exception as e:
                # Якщо виникла помилка при закритті, її можна обробити тут
                print(f"Error while closing file: {e}")

    def __del__(self) -> None:
        try:
            os.remove("file.txt")
        except FileNotFoundError:
            pass
