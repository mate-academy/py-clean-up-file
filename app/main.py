import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, file_type: Exception,
                 file_value: Exception, file_traceback: str) -> None:
        os.remove(self.filename)
