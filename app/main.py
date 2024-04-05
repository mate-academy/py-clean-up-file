from os import remove


class CleanUpFile:
    def __init__(self, filename: str = "file.txt") -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(
            self,
            exc_type: Exception,
            exc_val: Exception,
            exc_tb: str
    ) -> None:
        remove(self.filename)

    def __del__(self) -> None:
        pass
