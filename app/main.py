import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        try:
            print(open(self.filename, "r"), "content")
        except FileNotFoundError as error:
            print(error, "error")
            return None

    def __exit__(self) -> None:
        os.remove(self.filename)


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
