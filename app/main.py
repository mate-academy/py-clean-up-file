class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: type, exc_val: None, exc_tb: None) -> None:
        import os
        os.remove("file.txt")
