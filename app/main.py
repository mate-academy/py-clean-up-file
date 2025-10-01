import os


class CleanUpFile:
    """Context manager that removes the given file on exit."""

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        # Nothing special to return, but return self if needed
        return self

    def __exit__(
        self,
        exc_type: object,
        exc_val: object,
        exc_tb: object
    ) -> None:
        """Remove the file if it exists after context block ends."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
