import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.file_name = filename
        self.file_obj = open(self.file_name)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        os.remove(self.file_name)

