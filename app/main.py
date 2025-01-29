from pathlib import Path


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        file_path = Path(self.filename)
        if file_path.exists():
            file_path.unlink()
