import os.path


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)

        return False
