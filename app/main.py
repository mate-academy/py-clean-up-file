import os


class CleanUpFile:
    # write your code here
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> object:
        return self

    def __exit__(
            self,
            type_del: str,
            value_del: str,
            traceback_del: str
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
