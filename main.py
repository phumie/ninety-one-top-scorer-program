import sys

from utils.process_csv_string import process_csv_string
from utils.validators import validate_file

"""
    Reads a csv file and outputs the top scorers + marks

    Args:
    filename (str): Name of csv file.

    Returns:
    None
"""
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Program Arguments: python main.py *file.csv")
        sys.exit(1)

    filename = sys.argv[1]
    if validate_file(filename):
        with open(filename, 'r') as file:
            content = file.read()
            process_csv_string(content)
