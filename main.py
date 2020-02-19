from sys import argv
from pysplitlib.parse import parse_file


if __name__ == "__main__":
    FILE = argv[1]
    print(parse_file(FILE))
