import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        # Метод __enter__ ничего не делает в данном случае
        return self

    def __exit__(self, exc_type: BaseException,
                 exc_value: BaseException,
                 traceback: Exception) -> None:
        # Метод __exit__ выполняет удаление файла, если он существует
        if os.path.exists(self.filename):
            os.remove(self.filename)
