import os
import types


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None:
        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
        except Exception as e:
            print(
                f"Warning: Failed to delete '{self.filename}' due to "
                f"{type(e).__name__}: {e}"
            )
