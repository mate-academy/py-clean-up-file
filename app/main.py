import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self: str) -> str:
        return self

    def __exit__(self: str,
                 exc_type: type,
                 exc_val: Exception,
                 exc_tb: object) -> None:
        if os.path.exists(self.filename):
            try:
                os.remove(self.filename)
            except FileNotFoundError:
                pass
