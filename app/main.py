import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File '{self.filename}' has been removed.")


if __name__ == "__main__":
    filename = "file.txt"

    # Create a file for demonstration
    with open(filename, "w") as f:
        f.write("Hello, World!")

    # Use CleanUpFile context manager to ensure the file is removed
    with CleanUpFile(filename):
        # Any operations you want to perform with the file
        print(f"Working with {filename} inside the context manager.")

    # File should be removed after exiting the context manager
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
    else:
        print(f"File '{filename}' still exists.")
