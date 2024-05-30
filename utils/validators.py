import os
from sys import stderr


"""
    Checks if input file exists

    Args:
    filename (str): Name of csv file.

    Returns:
    boolean: True if file exists, False otherwise.
"""
def does_input_file_exist(filename: str) -> bool:
    if not os.path.exists(filename):
        stderr.write('InputFileError: file {} does not exist\n'.format(filename))
        return False
    return True


"""
    Checks if input file empty

    Args:
    filename (str): Name of csv file.

    Returns:
    boolean: True if file exists, False otherwise.
"""
def is_file_empty(filename: str) -> bool:
    if os.stat(filename).st_size == 0:
        stderr.write('InputFileError: cannot be empty\n')
        return False
    return True


def validate_file(filename: str) -> bool:
    if not does_input_file_exist(filename):
        return False
    if not is_file_empty(filename):
        return False
    return True
