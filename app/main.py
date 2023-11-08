import os


class CleanUpFile:
    def __init__(self, file_name: str, mode: str) -> None:
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self) -> None:
        self.file = open(self.file_name, self.mode)
        return  self.file

    def __exit__(self, exc_type: None,                  exc_val: None,                 exc_tb: None) -> None:
        self.file.close()

    def __del__(self) -> None:
        os.remove(self.file_name)
