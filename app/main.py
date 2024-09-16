import os


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        if not self.file.closed:
            self.file.close()
            os.remove(self.filename)
        return True


# with CleanUpFile("file.txt"):
#     with open("file.txt", "w") as file:
#         file.write("Hello Mate!")
