import os


class CleanUpFile:
    def __init__(self, namefile: str) -> None:
        self.namefile = namefile

    def __enter__(self) -> str:
        return self.namefile

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if os.path.exists(self.namefile):
            os.remove(self.namefile)
        return False


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
