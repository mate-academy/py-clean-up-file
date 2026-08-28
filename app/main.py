import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: type, exc_value: int, traceback: str) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


if __name__ == "__main__":
    with CleanUpFile("file.txt"):
        with open("file.txt", "w") as file:
            file.write("Hello Mate!")

    print("File cleanup complete.")
