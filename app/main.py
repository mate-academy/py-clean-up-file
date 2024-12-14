import os.path


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: BaseException,
            exc_val: BaseException,
            exc_tb: type
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File '{self.filename}' has been deleted.")
