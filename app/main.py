import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self,
                 exc_type: "type[BaseException] | None",
                 exc_val: "BaseException | None",
                 exc_tb: "any") -> None:
        os.remove(self.filename)
