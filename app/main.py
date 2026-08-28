import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> callable:
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        os.remove(self.filename)


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
