import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
        self,
        exc_type: type,
        exc_value: Exception,
        traceback: str
    ) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
