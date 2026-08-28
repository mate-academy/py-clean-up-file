from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self, exc_type: Exception,
            exc_value: Exception,
            exc_traceback: str
    ) -> None:
        remove(self.filename)
