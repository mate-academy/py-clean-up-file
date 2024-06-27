import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self, exc_type: Exception,
            exc_value: Exception, traceback: Exception
    ) -> None:
        try:
            with open(self.filename, "r"):
                pass
            os.remove(self.filename)
            print(f"File '{self.filename}' has been removed.")
        except FileNotFoundError:
            pass
