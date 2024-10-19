import os


class CleanUpFile:
    def __init__(
            self,
            filename: str
    ) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> object:
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self,
            exc_type: str,
            exc_value: str,
            exc_traceback: str
    ) -> None:
        self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
