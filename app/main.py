import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: None, exc_value: None, trace: None) -> None:
        self.file.close()
        os.remove(self.filename)

    def write(self, text: str) -> None:
        self.file.write(text)


with CleanUpFile("text.txt") as file:
    file.write("Hello, World!")
