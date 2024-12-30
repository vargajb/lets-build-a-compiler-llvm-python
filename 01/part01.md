## Part I: Introduction

The original compiler was implemented in a single source file. In this Python version, the implementation is divided into multiple source files to improve organization and maintainability:

### Files

*   **`cradle.py`:** The main program that coordinates the execution of the compiler.
*   **`code_processor.py`:** Contains a class for parsing input data and generating formatted code output. Parsing and code generation remain integrated in this version, following the approach of the original series.
*   **`scanner.py`:** Handles processing of the source code by reading it character by character.
    *   Changes from the original:
        *   The `GetChar` function has been renamed to `next_char`.
        *   The global variable `Look` has been replaced with the `peek_char` method.


### Overview

The primary goal of this compiler is to generate executable code. Input and output files can be specified using command-line arguments. This flexibility allows the compiler to process various input sources and generate corresponding outputs.

### Usage
The `cradle.py` script supports the following syntax:

`cradle.py [-h] [input] [--M68k OUTPUT_M68K] [--LLVM OUTPUT_LLVM]`

#### Positional Arguments
*   `input`: Input source (default: user input).

#### Options
*   `-h, --help`: Show this help message and exit.
*   `--M68k OUTPUT_M68K`: Specifies the output file or directs the output to `stdout` for M68000 code.
*   `--LLVM OUTPUT_LLVM`: Specifies the output file or directs the output to `stdout` for LLVM IR code.
---
<sub>Source: Adapted from Jack Crenshaw's "<a href="https://xmonader.github.io/letsbuildacompiler-pretty/tutor01_introduction.html" target="_blank">Let's Build a Compiler</a>" series.</sub>
