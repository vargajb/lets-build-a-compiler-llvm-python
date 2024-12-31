"""
Python port of Jack Crenshaw's "Let's Build a Compiler" series (1988-1995).

It was originally written in Pascal and modernized to generate LLVM IR code
instead of Motorola 68000.

@source: https://compilers.iecc.com/crenshaw/

Created on Sun Dec 15, 2024

@author: https://github.com/vargajb
"""
import sys
import traceback
import argparse
from scanner import Scanner
from code_processor import CodeProcessor

def read_input(path):
    """
    Read the input (either a file or user input).

    Parameters
    ----------
    path : str or None
        Specifies the input source.
        - If a string is provided, reads the content of the specified file.
        - If None, prompts the user to enter input interactively.

    Returns
    -------
    str
        The input data, either from the user or the input file.
    """
    if path is None:
        print("No input file provided, reading input from user.")
        return input("Please enter the input data: ")
    else:
        print(f"Reading input data from file: {path}")
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except IOError:
            print(f"Error reading file {path}.")
            raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A lightweight compiler that "
                                     "generates output for different targets.")
    parser.add_argument('input', type=str, nargs='?',
                        help='input source (default: user input)')
    args = parser.parse_args()
    try:
        input_data = read_input(args.input)
        scanner = Scanner(input_data)
        code_proc = CodeProcessor(scanner)
        code_proc.interpreter()
    except Exception as e:
        print(f"### Error: {e}")
        print("### Detailed traceback:")
        traceback.print_exc()
        print("### Exiting program.")
        sys.exit(1)
