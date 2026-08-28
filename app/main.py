import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: object | None,
            exc_val: object | None,
            exc_tb: object | None
    ) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            return
