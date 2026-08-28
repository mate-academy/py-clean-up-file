import os
from typing import Optional, Type


class CleanUpFile:
    """
    Context manager that removes a file after exiting the context.
    """

    def __init__(self, filename: str) -> None:
        """
        Initialize the context manager with a filename.

        Args:
            filename: Name of the file to clean up
        """
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        """
        Enter the context. No specific action needed.

        Returns:
            The context manager instance itself
        """
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[object]
    ) -> None:
        """
        Exit the context and remove the file if it exists.

        Args:
            exc_type: Exception type if an exception occurred
            exc_value: Exception value if an exception occurred
            traceback: Traceback if an exception occurred
        """
        if os.path.exists(self.filename):
            os.remove(self.filename)
