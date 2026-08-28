import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile | None":
        return self

    def __exit__(
            self,
            exc_type: BaseException | None,
            exc_val: BaseException | None,
            exc_tb: object | None
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Helo mate!")
