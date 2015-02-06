#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import csv
from argparse import ArgumentParser

#
# Command line options
#
parser = ArgumentParser(description="CSV Flattener")
parser.add_argument('-v', '--verbose', dest="verbose", action='count')
parser.add_argument('-c', dest="col", type=int, help="Split this col")
parser.add_argument('files', nargs='*',
                    help="The files to process. ")

def flatten(the_file, col = 0):
    """
    Flatten the CSV file.
    """
    with open(the_file, 'r') as csvfile:
        x = csv.reader(csvfile)
        for row in x:
            if row[col].find(",") >= 0:
                things = row[col].split(",")
                for t in things:
                    row[col]=t
                    print ', '.join(row)
            else:
                print ', '.join(row)

if __name__ == "__main__":
    args = parser.parse_args()

    for f in args.files:
        flatten(f, args.col - 1)

