import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        self.file = open(self.filename, "a+")
        return self

    def __exit__(
            self,
            exc_type: Exception,
            exc_val: Exception,
            exc_tb: Exception
    ) -> None:
        self.file.close()
        os.remove(self.filename)


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
