import os


class CleanUpFile:

    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> str:
        return self

    def __exit__(self, exc_type: any, exc_val: any, exc_tb: any) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
