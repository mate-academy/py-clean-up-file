import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
      self.file = None
      self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            os.remove(self.filename)
        except OSError:
            pass
        return False