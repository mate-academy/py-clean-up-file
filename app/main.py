import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename

    def __enter__(self) -> 'CleanUpFile':
        return self

    def __exit__(self, exc_type: type,
                 exc_value: BaseException,
                 traceback: None) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File '{self.filename}' has been removed.")
        else:
            print(f"File '{self.filename}' does not exist.")


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
