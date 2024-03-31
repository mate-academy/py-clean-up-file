import os


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self, method = "r"):
        return self

    def __exit__(self, exec_file, exec_value, traceback):
        os.remove(self.filename)
