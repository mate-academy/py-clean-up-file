import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        with open(self.filename, "w") as file_object:
            file_object.write("Hello Mate!")
        return self

    def __exit__(
            self,
            exc_typ: Exception,
            exc_val: Exception,
            exc_tb: Exception
    ) -> None:
        os.remove(self.filename)
