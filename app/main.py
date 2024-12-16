import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: type,
                 exc_value: Exception,
                 traceback: object) -> None:
        pass

    def __del__(self) -> None:
        os.remove(self.filename)
