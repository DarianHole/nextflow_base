#!/usr/bin/env python3

from Bio import seqIO
import pandas as pd
import argparse

def hello():
    return 'Hello'

def world():
    return 'World'

def main():
    print(hello() + ' ' + world())

if __name__ == "__main__":
    main()
