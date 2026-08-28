import os
from app.cleanup import CleanUpFile


def test_if_file_is_deleted():
    filename = "file.txt"

    with CleanUpFile(filename):
        with open(filename, "w") as f:
            f.write("Test data")

    assert not os.path.exists(filename)


def test_if_file_is_deleted_even_with_exception():
    filename = "file.txt"

    with open(filename, "w") as f:
        f.write("Test data")

    try:
        with CleanUpFile(filename):
            raise ValueError("Test error")
    except ValueError:
        pass

    assert not os.path.exists(filename)


def test_constructor_sets_filename():
    clean = CleanUpFile("file.txt")
    assert clean.filename == "file.txt"


def test_enter_returns_self():
    clean = CleanUpFile("file.txt")
    assert clean.__enter__() is clean
