import os


class CleanUpFile:
    def __init__(self, file_name: str):
        self.file_obj = open(file_name, "w")
        self.filename = file_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.file_obj.close(), os.remove(self.filename)
