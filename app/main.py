import os
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        # Nothing special to do on entering the context
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[object],
    ) -> bool:
        # Remove the file if it exists when leaving the context
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return False


# Example usage:
with open("file.txt", "w") as file:
    file.write(
        "Hello Mate! This line is now wrapped to stay under 79 characters."
    )

# After the with block ends,
# "file.txt" will be removed automatically
