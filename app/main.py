import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


if __name__ == "__main__":
    with CleanUpFile("file.txt") as manager:
        with open("file.txt", "w") as new_file:
            new_file.write("Hello, Mate!")
