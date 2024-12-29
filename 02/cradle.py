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
import ast
from sympy import sympify

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

def open_output(path):
    """
    Open the output destination (either a file or standard output).

    Parameters
    ----------
    path : str or None
        The path to the output file.
        - If None, returns None
        - If 'stdout', returns the standard output stream.
        - Otherwise, opens the specified file for writing and returns it.
    """
    if path is None:
        return None
    print(f"Writing output data to file: {path}")
    if path == 'stdout':
        return sys.stdout
    try:
        return open(path, "w", encoding="utf-8")
    except IOError:
        print(f"Error opening file {path} for writing.")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A lightweight compiler that "
                                     "generates output for different targets.")
    parser.add_argument('input', type=str, nargs='?',
                        help='input source (default: user input)')
    parser.add_argument('--M68k', type=str, dest='output_M68k',
                        help="output file or 'stdout' for M68000 code")
    parser.add_argument('--LLVM', type=str, dest='output_llvm',
                        help="output file or 'stdout' for LLVM IR code")
    args = parser.parse_args()
    if not (args.output_M68k or args.output_llvm):
        parser.error("At least one of --M68k or --LLVM must be specified.")
    try:
        input_data = read_input(args.input)
        scanner = Scanner(input_data)
        code_proc = CodeProcessor(scanner)
        if args.output_M68k:
            code_proc.set_m68k_code_output_file(open_output(args.output_M68k))
        if args.output_llvm:
            code_proc.set_llvm_code_output_file(open_output(args.output_llvm))
        code_proc.test_expression(input_data.splitlines())
        code_proc.close()
    except Exception as e:
        print(f"### Error: {e}")
        print("### Detailed traceback:")
        traceback.print_exc()
        print("### Exiting program.")
        sys.exit(1)
