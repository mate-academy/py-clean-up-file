import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> str:
        self.file = open(self.filename, "w+")
        return self.file

    def __exit__(self, exc_type: str, exc_val: str,
                 exc_tb: str) -> None:
        self.file.close()
        if os.path.exists(self.file):
            os.remove(self.file)
