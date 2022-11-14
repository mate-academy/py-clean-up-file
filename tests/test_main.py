import os.path

import pytest

from app.main import CleanUpFile

filename = "file.txt"


def test_if_file_is_deleted():
    with CleanUpFile(filename):
        with open(filename, "w") as f:
            f.write("Test data")

    assert os.path.exists(filename) is False, "File should be deleted"


def test_check_if_file_is_deleted_with_exception():
    with open(filename, "w") as f:
        f.write("Test data")

    try:
        with CleanUpFile(filename):
            raise ValueError("Test Value Error")

    except ValueError:
        pass

    assert os.path.exists(filename) is False, "File should be deleted despite exceptions"


def test_clean_up_file_constructor():
    clean_up = CleanUpFile(filename)
    assert clean_up.filename == "file.txt", "self.filename should equal filename given to constructor"


def test_clean_up_file_enter_method():
    clean_up = CleanUpFile(filename)
    assert clean_up.__enter__() == clean_up, "__enter__ should return class instance"
