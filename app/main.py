from typing import Self


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *files) -> None:
        import os

        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"Файл {self.filename} успішно видалено.")
        else:
            print(f"Файл {self.filename} не знайдено.")
