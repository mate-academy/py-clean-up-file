import os


class CleanUpFile:
    """Context manager that removes the specified file on exit."""

    def __init__(self, filename):
        """Initialize with the filename to clean up."""
        self.filename = filename

    def __enter__(self):
        """Enter the runtime context related to this object."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Remove the file if it exists when exiting the context."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return False
