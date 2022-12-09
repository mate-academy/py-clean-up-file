from os import remove


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: any, exc_val: any, exc_tb: any) -> None:
        remove(self.file_name)
