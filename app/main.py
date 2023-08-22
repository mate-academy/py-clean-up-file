import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        open("filename", "w")
        return self

    def __exit__(
            self,
            type_exception: str,
            value: str,
            traceback: str
    ) -> None:
        if os.path.isfile(self.filename):
            os.remove(self.filename)
