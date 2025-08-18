import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename


    def __enter__(self) -> "CleanUpFile":
        return self


    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return None


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("New file")
