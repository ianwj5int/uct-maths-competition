import argparse
import sys
import re


def convert_line(input_line):
    text_line = ''

    for c in input_line:
        if c < chr(32):
            # ignore low characters
            pass
        elif c <= chr(127):
            text_line += c
        else:
            # convert to ascii - WordStar adds 128 to the final char of each word
            text_line += chr(ord(c)-128)

    # tidy up line breaks, remove multiple spaces
    return re.sub('\r', '', re.sub(' +', ' ', text_line)) + '\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=argparse.FileType('r'), help='Input WordStar for DOS file')
    parser.add_argument('-o', '--out', default=sys.stdout, type=argparse.FileType('w'), help='Output text file (defaults to stdout)')
    args = parser.parse_args()
    for input_line in args.input_file:
        text_line = convert_line(input_line)
        if text_line:
            args.out.write(text_line)
    args.out.close()


if __name__ == "__main__":
    main()
