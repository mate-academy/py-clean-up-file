import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(
        self, exc_type: BaseException,
        exc_value: BaseException,
        traceback: object
    ) -> bool:
        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
        finally:
            return False


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
