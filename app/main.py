from os import remove


class CleanUpFile:
    def __init__(self, file_name: str):
        self.filename = file_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        remove(self.filename)
