import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> any:
        return self

    def __exit__(self,
                 exc_type : None,
                 exc_val : None,
                 exc_tb: None)\
            -> None:
        if os.path.exists(self.filename):
            try:
                os.remove(self.filename)
                print(f"Видаляю файл: {self.filename}")
            except FileNotFoundError:
                print("Помилка при видаленні")
