import os


class CleanUpFile:
    def __init__(self, name: str) -> None:
        self.filename = name

    def __enter__(self) -> object:
        return self

    def __exit__(
            self,
            exc_type: Exception,
            exc_val: Exception,
            exc_tb: Exception
    ) -> None:
        os.remove(self.filename)
