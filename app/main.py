import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        """Initialize with the filename to be cleaned up."""
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        """Enter the context and return the instance."""
        return self

    def __exit__(self, exc_type: type, exc_value: Exception, traceback: object) -> None:
        """Exit the context and remove the file if it exists."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(
                f"File {self.filename} has been removed."
            )  # Line break to avoid line too long warning.


# Example usage:
with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
