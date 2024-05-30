import os
from sys import stdout


"""
    Processes content from csv file and outputs names with top scores

    Args:
    content (str): Content from csv file.
    names (array): Names of top scorers.
    top_score (int): Highest score.

    Returns:
    None
"""
def process_csv_string(content: str):
    # split the csv string into an array
    content = content.strip().split('\n')
    names = []
    top_score = 0
    # process each row from csv file
    for row in content:
        # if the item is headers, do not process
        if 'First Name' in row:
            continue

        # split the row into an array in order to separate names and score
        data = row.strip().split(',')
        score = int(data[2])
        if score > top_score:
            top_score = score
            names = ["{} {}".format(data[0], data[1])]
        elif score == top_score:
            names.append("{} {}".format(data[0], data[1]))
    # sort the names of high scorers by alphabetical order
    names = sorted(names)
    # output names
    for name in names:
        stdout.write(f'{name}\n')
    # output score
    stdout.write(f'Score: {top_score}\n')
