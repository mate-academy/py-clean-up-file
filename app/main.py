import os


class CleanUpFile(object):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> callable:
        return self

    def __exit__(self,
                 exc_type: None, exc_value: None,
                 exc_traceback: None) -> None:
        os.remove(self.filename)
