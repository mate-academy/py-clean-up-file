import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: object, exc_val: object,
                 exc_tb: object) -> None:
        if os.path.isfile(self.filename):
            os.remove(self.filename)


if __name__ == "__main__":
    with CleanUpFile("file.txt"):
        with open("file.txt", "w") as file_obj:
            file_obj.write("Hello Mate!")
