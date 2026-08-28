import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        # Nothing special to return; just enter the context.
        return self

    def __exit__(self, exc_type: Exception,
                 exc_val: Exception, exc_tb: Exception) -> None:
        # Remove the file if it exists
        if os.path.exists(self.filename):
            os.remove(self.filename)
