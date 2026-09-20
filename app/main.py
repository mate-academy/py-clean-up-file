import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        try:
            open(self.filename, "r")
        except FileNotFoundError:
            print("File not found")
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        os.remove("file.txt")


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
