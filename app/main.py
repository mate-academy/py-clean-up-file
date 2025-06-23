import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self,
                 exc_type: None,
                 exc_value: None,
                 traceback: None) -> bool:  # Мають
        # бути прописані в ексіті всі ці 4 параметри,
        # навіть якщо не всі використовуються
        if os.path.exists(self.filename):  # Перевіряє існування саме файлу
            os.remove(self.filename)
        return False  # Без цього виключення можуть бути "приглушені",
        # тобто не передані далі.
