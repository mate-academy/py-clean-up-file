class CleanUpFile:
    def __init__(self, name: str) -> None:
        self.name = name
        self.file = None

    def __enter__(self):
        self.file = open(self.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __del__(self):
        self.file.close()
