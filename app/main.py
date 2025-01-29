from pathlib import Path


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self,
                 exc_type: type,
                 exc_val: Exception,
                 exc_tb: object
                 ) -> None:
        file_path = Path(self.filename)
        if file_path.exists():
            file_path.unlink()
