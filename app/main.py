import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        with open(self.filename, "w") as file:
            file.write("Некоторые начальные данные")
            return self

    def __exit__(self, exc_type: int, exc_val: int, exc_tb: int) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"Файл {self.filename} удалён.")
        else:
            print("Файл не существует.")
