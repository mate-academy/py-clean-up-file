import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self,
            exc_type: str,
            exc_val: str,
            exc_tb: str
    ) -> None:
        if self.file and not self.file.closed:
            self.file.close()

    def __del__(self) -> None:
        if self.file and not self.file.closed:
            self.file.close()

        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
