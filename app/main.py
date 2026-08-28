import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self,
                 exc_type: Exception,
                 exc_val: Exception,
                 exc_tb: Exception) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            print(f"File {self.filename} doesn't exist")
