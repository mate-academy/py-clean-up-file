import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        self.file_obj = open(self.filename, "a")
        return self

    def __exit__(
            self,
            exc_type: type,
            exc_value: Exception,
            traceback: object
    ) -> None:
        self.file_obj.close()

        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
