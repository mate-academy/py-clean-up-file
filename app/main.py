import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        if not isinstance(self.filename, str):
            raise TypeError("filename must be a string")

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self,
                 exc_type: type[BaseException] | None,
                 exc_val: BaseException | None,
                 exc_tb: object | None) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        else:
            return


with CleanUpFile("file.txt"):
    with open("file.txt", "a") as file:
        file.write("Hello Mate!")
    with open("file.txt", "r") as file:
        print(file.read())
