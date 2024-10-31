import os
class CleanUpFile:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        # Return the filename for use in the with block, if needed
        return self.filename

    def __exit__(self, exc_type, exc_value, traceback):
        # Remove the file if it exists
        if os.path.exists(self.filename):
            os.remove(self.filename)
