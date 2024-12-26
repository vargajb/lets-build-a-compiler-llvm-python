"""Parsing input data and generating formatted code output."""
import sys

class CodeProcessor:
    """
    A class for parsing input data and generating formatted code output.

    This class integrates parsing and code generation, using an internal
    scanner for processing input and providing methods to emit code to an
    output stream.
    You can specify output files by calling either `set_m68k_code_output_file`,
    `set_llvm_code_output_file`, or both, depending on which output formats you
    need.

    Parameters
    ----------
        scanner (Scanner): A scanner instance used for parsing input data.
    """

    def __init__(self, scanner):
        self.__scanner = scanner
        self.__file_m68k = None
        self.__file_llvm = None

    def set_m68k_code_output_file(self, file):
        """Set output file for M68k code."""
        self.__file_m68k = file

    def set_llvm_code_output_file(self, file):
        """Set output file for LLVM IR code."""
        self.__file_llvm = file

    def __close(self, file):
        if file is not None and file is not sys.stdout:
            file.close()

    def close(self):
        """Close output files."""
        self.__close(self.__file_m68k)
        self.__close(self.__file_llvm)

    def __emit(self, file, s, comment='', indent=1):
        """Output a string with a tab and aligned trailing comments."""
        tab_size = 4
        base_length = len("\t") + len(s) + tab_size
        padding = max(35 - base_length, 1)
        aligned_comment = f"{' ' * padding} ; {comment}" if comment else ""
        print(f"{' ' * indent * 4}{s}{aligned_comment}", end='', file=file)

    def __emit_ln(self, file, s, comment='', indent=1):
        """Output a string with a tab and a newline."""
        self.__emit(file, s, comment, indent)
        print(file=file)

    def emit_ln_m68k(self, s, comment='', indent=1):
        """Output a string targeting Motorola 68000 code with newline."""
        if self.__file_m68k:
            self.__emit_ln(self.__file_m68k, s, comment)

    def emit_ln_llvm(self, s, comment='', indent=1):
        """Output a string targeting LLVM IR code with newline."""
        if self.__file_llvm:
            self.__emit_ln(self.__file_llvm, s, comment, indent)
