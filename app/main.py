import os


class CleanUpFile:
    filename = None

    def __init__(self, file_name: str):
        self.filename = file_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        file_path = "E:\\projects\\py-clean-up-file\\file.txt"
        os.remove(file_path)
