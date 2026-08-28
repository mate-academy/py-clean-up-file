import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename: str = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: BaseException,
            exc_val: BaseException,
            exc_tb: bool
    ) -> None:
        if self.filename and os.path.exists(self.filename):
            os.remove(self.filename)
