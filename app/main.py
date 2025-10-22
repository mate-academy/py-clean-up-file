import os

class CleanUpFile:
    """
    Context manager that removes the specified file upon exiting the context
    if it exists.
    """

    def __init__(self, filename):
        # Accept only the filename to manage
        self.filename = filename

    def __enter__(self):
        # Nothing special to prepare; return self to allow optional usage
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # On exit, remove the file if it exists
        if os.path.exists(self.filename):
            os.remove(self.filename)
        # Do not suppress exceptions from the context block
        return False
