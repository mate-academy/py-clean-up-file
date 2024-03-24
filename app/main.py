import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, p2: any, p3: any, p4: any) -> None:
        self.file.close()
        os.remove(self.filename)
