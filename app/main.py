import os.path


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: type,
            exc_val: BaseException,
            exc_tb: any
    ) -> None:
        if self.filename and os.path.exists(self.filename):
            os.remove(self.filename)
