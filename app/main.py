class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: any, exc_val: any, exc_tb: any) -> None:
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)
