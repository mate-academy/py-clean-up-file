import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(
        self,
        exc_type: object,
        exc_val: object,
        exc_tb: object
    ) -> None:
        pass

    def __del__(self) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
