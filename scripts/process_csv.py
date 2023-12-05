# Standard packages
import os
# Installed packages
import chardet
import pandas as pd


def convert_csv_to_utf8(filepath: str):
    """Convert CSV file to UTF-8 encoding.
    Args:
        filepath: Path to CSV file.
    """
    # get encoding of CSV file
    with open(filepath, 'rb') as file:
        encoding = chardet.detect(file.read())['encoding']

    # convert CSV file to UTF-8 encoding
    try:
        # read CSV file
        df = pd.read_csv(filepath, encoding=encoding)
        # save CSV file with UTF-8 encoding
        df.to_csv(filepath, encoding='utf-8', index=False)
        print(f'File {filepath} converted to UTF-8.')
    except Exception as e:
        print(f'Failed to convert {filepath}: {e}')


def convert_all_csv_to_utf8(search_dir: str):
    """Convert all CSV files in a directory to UTF-8 encoding.
    Args:
        search_dir: Directory to search for CSV files.
    """
    # loop through all files in current directory and subdirectories
    for subdir, _, files in os.walk(search_dir):
        for file in files:
            filepath = os.path.join(subdir, file)

            # check if the file is a CSV file
            if filepath.endswith('.csv'):
                # convert the file to UTF-8
                convert_csv_to_utf8(filepath)


if __name__ == '__main__':
    # initialize search directory
    search_dir = './database/files'
    # convert all CSV files in search directory to UTF-8
    convert_all_csv_to_utf8(search_dir)
