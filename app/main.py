from os import remove, path


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: Exception, exc_value: Exception,
                 exc_traceback: Exception) -> None:
        if path.exists(self.filename):
            remove(self.filename)
