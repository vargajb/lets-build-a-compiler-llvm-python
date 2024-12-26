## Part I: Introduction

Originally, the compiler was written in a single source file. However, in this Python version, it's split into multiple source files for better organization:

*   **`cradle.py`:** The main program that coordinates the execution of the compiler.
*   **`scanner.py`:** Handles processing of the source code by reading it character by character.
    *   Changes from the original:
        *   `GetChar` is renamed to `next_char`.
        *   Instead of the global variable `Look`, the `peek_char` method should be used.
*   **`code_processor.py`:** Contains a class for parsing input data and generating formatted code output. In the original series, parsing and code generation were not separated, and this version follows the same approach.

## Compiler Overview

The primary goal of this compiler is to generate executable code. To achieve this, input and output files can be specified using command-line arguments.

## Usage
cradle.py [-h] [--M68k OUTPUT_M68K] [--LLVM OUTPUT_LLVM] [input]

### Positional Arguments
*   `input`: Input source (default: user input).

### Options
*   `-h, --help`: Show this help message and exit.
*   `--M68k OUTPUT_M68K`: Output file or `stdout` for M68000 code.
*   `--LLVM OUTPUT_LLVM`: Output file or `stdout` for LLVM IR code.
