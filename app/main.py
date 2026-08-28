import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self,
                 exc_type: str,
                 exc_value: str,
                 exc_traceback: str
                 ) -> bool:
        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
        except OSError:
            pass
        return False


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
    pass
