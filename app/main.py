from os import remove


class CleanUpFile:
    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_mode = "a"
        self.file = None

    def __enter__(self) -> None:
        self.file = open(self.filename, self.file_mode)
        return self

    def __exit__(self, exc_type: Exception,
                 exc_val: Exception,
                 exc_tb: Exception) -> None:
        self.file.close()
        remove(self.filename)
