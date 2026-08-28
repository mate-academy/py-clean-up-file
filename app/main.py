import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        try:
            self.file = open(self.filename)
            return self
        except FileNotFoundError:
            return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        try:
            self.file.close()
        except Exception:
            pass

    def __del__(self) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
