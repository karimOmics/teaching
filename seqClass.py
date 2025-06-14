#!/usr/bin/env python

"""
seqClass.py

Classifies a sequence as DNA or RNA based on nucleotide composition.
Also optionally searches for a motif within the sequence.

Usage:
    python seqClass.py -s <sequence> [-m <motif>]
"""

import sys
import re
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
    parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
    parser.add_argument("-m", "--motif", type=str, required=False, help="Motif to search for")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    seq = args.seq.upper()

    # Validate sequence: only A,C,G,T,U allowed
    if not re.match(r'^[ACGTU]+$', seq):
        print("The sequence contains invalid characters. Only A, C, G, T, U are allowed.")
        sys.exit(1)

    # Check for mixed T and U - invalid biologically
    if 'T' in seq and 'U' in seq:
        print("Invalid sequence: contains both T (DNA) and U (RNA).")
        sys.exit(1)

    # Classify sequence
    if 'T' in seq:
        print("The sequence is classified as DNA.")
    elif 'U' in seq:
        print("The sequence is classified as RNA.")
    else:
        print("The sequence is ambiguous: contains only A, C, G (could be DNA or RNA).")

    # Motif search (case insensitive)
    if args.motif:
        motif = args.motif.upper()
        print(f'Searching for motif "{motif}" in sequence...')
        if re.search(motif, seq):
            print("Motif FOUND")
        else:
            print("Motif NOT FOUND")

if __name__ == "__main__":
    main()
