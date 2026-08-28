import os
from binascii import Error


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: Exception,
            exc_value: Error,
            traceback: Exception
    ) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return False
