import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        """
        Initialize the context manager with the filename.
        """
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        """
        Enter method returns the context manager instance.
        """
        return self

    def __exit__(
        self, exc_type: type, exc_value: Exception, traceback: object
    ) -> None:
        """
        Exit method ensures the file is deleted if it exists.
        """
        if os.path.exists(self.filename):
            os.remove(self.filename)
