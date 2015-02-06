#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import csv
import sys
from argparse import ArgumentParser

#
# Command line options
#
parser = ArgumentParser(description="CSV Widener")
parser.add_argument('-v', '--verbose', dest="verbose", action='count')
parser.add_argument('-c', dest="col", type=int, help="Split this col")
parser.add_argument('-s', "--seperator", default=".", help="Seperator to use")
parser.add_argument('files', nargs='*',
                    help="The files to process. ")

def widen(the_file, sep, col = 0):
    """
    Widen the CSV file.
    """
    with open(the_file, 'r') as csvfile:
        infile = csv.reader(csvfile)
        outfile = csv.writer(sys.stdout)
        for row in infile:
            # cell to widen
            cell = row[col]
            pos = cell.rfind(sep)
            if pos>0:
                # split col into col and col + 1
                left = cell[:pos]
                right = cell[pos+1:]
            else:
                # just insert a blank cell after col
                left = cell
                right = ""
            # tweak the row
            row[col] = left
            row.insert(col+1, right)
            outfile.writerow(row)

if __name__ == "__main__":
    args = parser.parse_args()

    for f in args.files:
        widen(f, args.seperator, args.col - 1)
