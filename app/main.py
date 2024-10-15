import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        open(self.filename, "w")
        return self

    def __exit__(
            self,
            exc_type: BaseException | None,
            exc_val: BaseException | None,
            exc_tb: BaseException | None
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
